import argparse
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import available_functions, call_function
from prompts import system_prompt
from config import MAX_ITERS


def main():
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    for _ in range(MAX_ITERS):
        try:
            final_response = generate_content(client, messages, args.verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                return
        except Exception as e:
            print(f"Error in generate_content: {e}")

    print(f"Maximum iterations ({MAX_ITERS}) reached")
    sys.exit(1)


def call_model(functions, system_instructions):
    pass

def generate_content(client, messages, verbose):
    # call the model, handle responses, etc.
    function_result_response_list = []
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if response.candidates:
        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate)

    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        print("Response:")
        print(response.text)
        return

    for function_call in response.function_calls:
        function_call_result = call_function(function_call, verbose)
        if function_call_result.parts is None:
            raise TypeError("function_call_results has an empty parts list")
        if function_call_result.parts[0].function_response is None:
            raise TypeError("function_call_results is not FunctionResponse object")
        if function_call_result.parts[0].function_response.response is None:
            raise TypeError("function_call_results has no response")
        
        function_result_response_list.append(function_call_result.parts[0]) # Only if no errors
    
        messages.append(types.Content(role="user", parts=function))
        
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")



if __name__ == "__main__": # when file is run
    main()
    