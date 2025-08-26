import google.generativeai as genai
from config.settings import GEMINI_API_KEY

class GeminiChatBot:
    def __init__(self, model_name="gemini-2.5-pro"):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(model_name)

    def chat(self, message: str, history: list = None) -> str:
        if history is None:
            history = []
        response = self.model.generate_content(
            [*history, {"role": "user", "parts": [message]}]
        )
        print(response)
        # ✅ Safely extract the output text
        if response.candidates and response.candidates[0].content.parts:
            return "".join(
                part.text for part in response.candidates[0].content.parts if hasattr(part, "text")
            )
        else:
            return "(No response generated — model stopped early)"
