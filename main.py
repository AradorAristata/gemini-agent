import os
import argparse
from prompts import system_prompt
from functions.call_function import available_functions, call_function
from dotenv import load_dotenv
from google import genai
from google.genai import types


def call_model(client,messages):
    return client.models.generate_content(
         model='gemini-2.5-flash', contents=messages, 
         config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt, temperature=0.2))

def handle_response(response, args):
    
    if response.usage_metadata == None:
        raise RuntimeError("Usage metadata not found in response")

    if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    if response.function_calls == None:
        print("Response:", response.text)
        return None
    else:
        function_results = []
        #print(response.function_calls)
        for each in response.function_calls:
            function_call_result = call_function(each, verbose=args.verbose)
            if function_call_result.parts == None:
                raise Exception("Function call result parts not found")
            if function_call_result.parts[0].function_response == None:
                raise Exception("Function response not found in function call result parts")
            if function_call_result.parts[0].function_response.response == None:    
                raise Exception("Response not found in function response in function call result parts")
            
            function_results.append(function_call_result.parts[0])
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
        return function_results

            
            

def main():
    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("GEMINI_API_KEY not found in environment variables")
    client = genai.Client(api_key=api_key)

    for _ in range(20):
        response = call_model(client, messages)
        if response.candidates == None or len(response.candidates) == 0:
            raise RuntimeError("Candidates not found in response")
        
        for each in response.candidates:
            messages.append(each.content)

        function_responses = handle_response(response, args)
        if function_responses != None:
            messages.append(types.Content(role="user", parts=function_responses))
        else:
            break

        if _ == 19:
            print("Max iterations reached, stopping conversation.")
            exit(1)

if __name__ == "__main__":
    main()
