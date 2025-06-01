from dotenv import load_dotenv
import os

from google import genai
from google.genai import types

load_dotenv()  # load environment variables from .env file


def run_chat_agent():
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    chat_history = []

    while True:
        user_input = input("You: ")

        chat_history.append({"speaker": "User", "text": user_input})

        if user_input.lower() in ["exit", "quit"]:  # quit the chat agent
            print("Gemini: Goodbye!")
            break

        # generate response using Gemini model
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[f"{hist['speaker']}: {hist['text']}" for hist in chat_history],
            config=types.GenerateContentConfig(
                system_instruction="You are a helpful AI chat assistant provided with the context of the conversation.",
            ),
        )

        response_text = response.text.lstrip("Gemini: ").strip()
        print("Gemini:", response_text)
        chat_history.append({"speaker": "Gemini", "text": response_text})


if __name__ == "__main__":
    run_chat_agent()
