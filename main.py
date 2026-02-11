import os
import argparse
from dotenv import load_dotenv
from google import genai


def main():
    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`
    print(f"User prompt: {args.user_prompt}")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("GEMINI_API_KEY not found in environment variables")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
    model='gemini-2.5-flash', contents=args.user_prompt)

    if response.usage_metadata == None:
        raise RuntimeError("Usage metadata not found in response")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:", response.text)

    


if __name__ == "__main__":
    main()
