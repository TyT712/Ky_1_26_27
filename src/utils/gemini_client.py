"""Gemini API client wrapper for Academic Knowledge & Study System."""

import os
import json
import base64
from typing import Optional, Dict, Any, List
from pathlib import Path
import httpx

class GeminiClient:
    """Client wrapper for Google Gemini API using httpx."""

    def __init__(self, api_key: Optional[str] = None, model: str = "gemini-2.5-flash"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model = model
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"

    def is_configured(self) -> bool:
        """Check if GEMINI_API_KEY is present."""
        return bool(self.api_key and len(self.api_key.strip()) > 5)

    def generate_content(
        self,
        prompt: str,
        system_instruction: Optional[str] = None,
        temperature: float = 0.2,
        max_output_tokens: int = 4096,
        response_mime_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """Generate text response using Gemini API."""
        if not self.is_configured():
            return {
                "success": False,
                "error": "GEMINI_API_KEY is not configured. Please set the environment variable.",
                "text": ""
            }

        url = f"{self.base_url}/models/{self.model}:generateContent?key={self.api_key}"
        
        contents = [{"parts": [{"text": prompt}]}]
        
        generation_config: Dict[str, Any] = {
            "temperature": temperature,
            "maxOutputTokens": max_output_tokens
        }
        if response_mime_type:
            generation_config["responseMimeType"] = response_mime_type

        payload: Dict[str, Any] = {
            "contents": contents,
            "generationConfig": generation_config
        }

        if system_instruction:
            payload["systemInstruction"] = {
                "parts": [{"text": system_instruction}]
            }

        try:
            with httpx.Client(timeout=60.0) as client:
                res = client.post(url, json=payload)
                res.raise_for_status()
                data = res.json()
                
                candidates = data.get("candidates", [])
                if candidates and "content" in candidates[0]:
                    parts = candidates[0]["content"].get("parts", [])
                    output_text = "".join(part.get("text", "") for part in parts)
                    return {
                        "success": True,
                        "text": output_text,
                        "raw": data
                    }
                else:
                    return {
                        "success": False,
                        "error": "No candidates returned by Gemini API.",
                        "text": ""
                    }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "text": ""
            }

    def parse_pdf_with_gemini(
        self, 
        pdf_path: str, 
        prompt: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Multimodal PDF parsing: Sends PDF to Gemini to extract high-fidelity 
        Markdown with table formatting, LaTeX math formulas, and hierarchy.
        """
        if not self.is_configured():
            return {
                "success": False,
                "error": "GEMINI_API_KEY is not set. Multimodal PDF parsing requires Gemini API."
            }

        file_path = Path(pdf_path)
        if not file_path.exists():
            return {"success": False, "error": f"File not found: {pdf_path}"}

        pdf_bytes = file_path.read_bytes()
        pdf_b64 = base64.b64encode(pdf_bytes).decode("utf-8")

        default_prompt = (
            "Trích xuất toàn bộ nội dung giáo trình học thuật này sang định dạng Markdown chuẩn:\n"
            "1. Bảo toàn chính xác các cấp độ tiêu đề (# Chương, ## Mục, ### Tiểu mục).\n"
            "2. Chuyển đổi toàn bộ công thức toán học, vật lý, hóa học sang chuẩn LaTeX ($inline$ và $$block$$).\n"
            "3. Giữ nguyên bảng biểu, code block (có chú thích ngôn ngữ).\n"
            "4. Đánh dấu vị trí trang bằng thẻ: <!-- PAGE X --> (với X là số trang thực tế).\n"
            "5. Không tóm tắt hoặc bỏ sót kiến thức lý thuyết quan trọng."
        )

        url = f"{self.base_url}/models/{self.model}:generateContent?key={self.api_key}"
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "inlineData": {
                                "mimeType": "application/pdf",
                                "data": pdf_b64
                            }
                        },
                        {"text": prompt or default_prompt}
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.1,
                "maxOutputTokens": 8192
            }
        }

        try:
            with httpx.Client(timeout=120.0) as client:
                res = client.post(url, json=payload)
                res.raise_for_status()
                data = res.json()
                
                candidates = data.get("candidates", [])
                if candidates and "content" in candidates[0]:
                    parts = candidates[0]["content"].get("parts", [])
                    output_text = "".join(part.get("text", "") for part in parts)
                    return {"success": True, "markdown": output_text}
                return {"success": False, "error": "No content generated."}
        except Exception as e:
            return {"success": False, "error": str(e)}
