"""Study Assistant Skill: Hỗ trợ ôn tập, giải bài tập và sinh câu hỏi trắc nghiệm bám sát giáo trình."""

import os
import sys
import argparse
from pathlib import Path
from typing import Dict, Any, Optional

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from src.skills.knowledge_retriever import AcademicRetriever
from src.utils.gemini_client import GeminiClient

SYSTEM_INSTRUCTION = """Bạn là Trợ lý Học thuật Thông minh (Academic Study Assistant) được hỗ trợ bởi hệ thống Antigravity.
Nhiệm vụ của bạn là hỗ trợ sinh viên học tập, ôn thi và giải bài tập BÁM SÁT 100% VÀO GIÁO TRÌNH ĐƯỢC CẤP.

CÁC NGUYÊN TẮC CỐT LÕI (BẮT BUỘC TUÂN THỦ):
1. ZERO HALLUCINATION & STRICT GROUNDING:
   - Chỉ trả lời dựa trên các đoạn trích từ [GIÁO TRÌNH] và [TÓM TẮT NOTEBOOKLM] được cung cấp trong ngữ cảnh.
   - Luôn ghi rõ nguồn trích dẫn học thuật ở đầu hoặc cuối câu trả lời dạng: [Môn học: ... | Tài liệu: ... | Mục: ...].
   - Nếu trong tài liệu không có thông tin giải quyết câu hỏi, BẮT BUỘC nói rõ: "Giáo trình hiện tại không cung cấp nội dung này" trước khi đưa ra gợi ý mở rộng (nếu có, và phải ghi rõ nhãn [Kiến thức mở rộng tham khảo]).

2. ĐỊNH DẠNG HỌC THUẬT:
   - Dùng chuẩn LaTeX ($inline$ và $$block$$) cho tất cả công thức toán, lý, hóa.
   - Trình bày lời giải bài tập theo từng bước mạch lạc:
     * Bước 1: Xác định yêu cầu và giả thiết.
     * Bước 2: Nhắc lại công thức / định lý trong giáo trình kèm trích dẫn.
     * Bước 3: Các bước biến đổi và tính toán cụ thể.
     * Bước 4: Kết luận và lưu ý lỗi sai thường gặp.

3. TỰ ĐỘNG SINH CÂU HỎI ÔN TẬP:
   - Mỗi câu hỏi trắc nghiệm phải có 4 lựa chọn (A, B, C, D), đáp án chính xác và phần giải thích đối chiếu với mục nào trong giáo trình.
"""

class StudyAssistant:
    """Skill hỗ trợ học tập, sinh câu hỏi và giải bài tập bám sát giáo trình."""

    def __init__(
        self,
        retriever: Optional[AcademicRetriever] = None,
        gemini_client: Optional[GeminiClient] = None
    ):
        self.retriever = retriever or AcademicRetriever()
        self.gemini_client = gemini_client or GeminiClient()

    def _call_model_or_fallback(self, prompt: str) -> str:
        """Call Gemini API or provide structured academic fallback if API key is not yet set."""
        if self.gemini_client.is_configured():
            res = self.gemini_client.generate_content(
                prompt=prompt,
                system_instruction=SYSTEM_INSTRUCTION
            )
            if res.get("success"):
                return res.get("text", "")
            return f"[!] Lỗi kết nối mô hình: {res.get('error')}"

        # Fallback when GEMINI_API_KEY is not set: return formatted context & instructions
        return (
            "### [CHẾ ĐỘ NỘI BỘ - CHƯA CẤU HÌNH GEMINI_API_KEY]\n\n"
            "> Vui lòng đặt biến môi trường `GEMINI_API_KEY` để nhận phản hồi phân tích tự động từ LLM.\n\n"
            "Dưới đây là ngữ cảnh trích xuất từ kho học liệu đối chiếu:\n\n"
            f"{prompt}"
        )

    def solve_exercise(self, problem_statement: str, subject_code: Optional[str] = None) -> Dict[str, Any]:
        """Giải bài tập từng bước có đối chiếu định lý, công thức trong giáo trình."""
        retrieval = self.retriever.dual_retrieve(problem_statement, subject_code=subject_code, top_k=4)
        context = retrieval.get("consolidated_context", "")

        prompt = (
            f"ĐỀ BÀI TẬP CẦN GIẢI:\n{problem_statement}\n\n"
            f"NGỮ CẢNH TÀI LIỆU HỌC THUẬT ĐƯỢC TRÍCH XUẤT:\n{context}\n\n"
            "YÊU CẦU: Hãy giải bài tập trên theo chuẩn 4 bước học thuật, trích dẫn rõ công thức và định lý từ ngữ cảnh được cung cấp."
        )

        solution = self._call_model_or_fallback(prompt)
        return {
            "task": "solve_exercise",
            "problem": problem_statement,
            "subject_code": subject_code,
            "retrieval_matches": retrieval.get("total_matches", 0),
            "solution": solution
        }

    def generate_quiz(
        self,
        topic: str,
        subject_code: Optional[str] = None,
        num_questions: int = 3,
        difficulty: str = "intermediate"
    ) -> Dict[str, Any]:
        """Sinh bộ câu hỏi trắc nghiệm/tự luận ôn tập bám sát giáo trình."""
        retrieval = self.retriever.dual_retrieve(topic, subject_code=subject_code, top_k=4)
        context = retrieval.get("consolidated_context", "")

        prompt = (
            f"CHỦ ĐỀ ÔN TẬP: {topic}\n"
            f"ĐỘ KHÓ: {difficulty}\n"
            f"SỐ LƯỢNG CÂU HỎI: {num_questions}\n\n"
            f"TÀI LIỆU THAM CHIẾU TỪ GIÁO TRÌNH & NOTEBOOKLM:\n{context}\n\n"
            "YÊU CẦU: Hãy tạo bộ câu hỏi ôn tập bám sát tài liệu trên. Mỗi câu hỏi gồm:\n"
            "- Đề câu hỏi rõ ràng\n"
            "- 4 phương án (A, B, C, D)\n"
            "- Đáp án đúng\n"
            "- Giải thích chi tiết và trích dẫn mục tài liệu làm căn cứ."
        )

        quiz = self._call_model_or_fallback(prompt)
        return {
            "task": "generate_quiz",
            "topic": topic,
            "subject_code": subject_code,
            "quiz": quiz
        }

    def explain_concept(self, concept: str, subject_code: Optional[str] = None) -> Dict[str, Any]:
        """Giải thích khái niệm học thuật chuyên sâu kèm ví dụ trực quan và công thức."""
        retrieval = self.retriever.dual_retrieve(concept, subject_code=subject_code, top_k=4)
        context = retrieval.get("consolidated_context", "")

        prompt = (
            f"KHÁI NIỆM CẦN GIẢI THÍCH: {concept}\n\n"
            f"NGỮ CẢNH GIÁO TRÌNH GỐC & TÓM TẮT:\n{context}\n\n"
            "YÊU CẦU: Giải thích khái niệm trên một cách dễ hiểu, đầy đủ định nghĩa toán/học thuật chuẩn, ví dụ minh họa và mối liên hệ với các phần khác trong môn học."
        )

        explanation = self._call_model_or_fallback(prompt)
        return {
            "task": "explain_concept",
            "concept": concept,
            "subject_code": subject_code,
            "explanation": explanation
        }

def main():
    parser = argparse.ArgumentParser(description="Skill Study Assistant")
    subparsers = parser.add_subparsers(dest="action", help="Tác vụ học tập")

    # Solve
    solve_p = subparsers.add_parser("solve", help="Giải bài tập")
    solve_p.add_argument("query", type=str, help="Đề bài tập")
    solve_p.add_argument("--subject", type=str, default=None, help="Mã môn học")

    # Quiz
    quiz_p = subparsers.add_parser("quiz", help="Tạo câu hỏi trắc nghiệm")
    quiz_p.add_argument("topic", type=str, help="Chủ đề ôn tập")
    quiz_p.add_argument("--subject", type=str, default=None, help="Mã môn học")
    quiz_p.add_argument("-n", "--num", type=int, default=3, help="Số câu hỏi")

    # Explain
    explain_p = subparsers.add_parser("explain", help="Giải thích khái niệm")
    explain_p.add_argument("concept", type=str, help="Tên khái niệm")
    explain_p.add_argument("--subject", type=str, default=None, help="Mã môn học")

    args = parser.parse_args()
    assistant = StudyAssistant()

    if args.action == "solve":
        res = assistant.solve_exercise(args.query, subject_code=args.subject)
        print("\n=== LỜI GIẢI BÀI TẬP BÁM SÁT GIÁO TRÌNH ===\n")
        print(res["solution"])
    elif args.action == "quiz":
        res = assistant.generate_quiz(args.topic, subject_code=args.subject, num_questions=args.num)
        print("\n=== BỘ CÂU HỎI ÔN TẬP TỰ ĐỘNG ===\n")
        print(res["quiz"])
    elif args.action == "explain":
        res = assistant.explain_concept(args.concept, subject_code=args.subject)
        print("\n=== GIẢI THÍCH KHÁI NIỆM HỌC THUẬT ===\n")
        print(res["explanation"])
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
