"""Gemini API client wrapper for Academic Knowledge & Study System."""

import os
import json
from typing import Optional, Dict, Any, List
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
