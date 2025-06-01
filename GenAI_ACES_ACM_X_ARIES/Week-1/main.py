from dotenv import load_dotenv
import os

from google import genai
from google.genai import types

load_dotenv()


def run_chat_agent():
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    chat_history = []

    while True:
        user_input = input("You: ")

        chat_history.append({"speaker": "User", "text": user_input})

        if user_input.lower() in ["exit", "quit"]:
            print("Gemini: Goodbye!")
            break

        print("Gemini:", end=" ")

        response = client.models.generate_content_stream(
            model="gemini-1.5-flash",
            contents=[f"{hist['speaker']}: {hist['text']}" for hist in chat_history]
            + [f"User: {user_input}"],
            config=types.GenerateContentConfig(
                system_instruction="You are a helpful AI chat assistant provided with the context of the conversation.",
            ),
        )

        response_text = ""

        for chunk in response:
            response_text += chunk.text
            print(chunk.text, end="")

        chat_history.append({"speaker": "Gemini", "text": response_text})


if __name__ == "__main__":
    run_chat_agent()
