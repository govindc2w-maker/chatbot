import pytest
from core.chatbot import GeminiChatBot

def test_chat_response():
    bot = GeminiChatBot()
    response = bot.chat("Hello")
    assert isinstance(response, str)
    assert len(response) > 0
