import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
import sys
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise Exception("missing api key")

# Parse and add the arguments
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

# Create the prompt that it will use
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


if args.user_prompt is None:
    print("Error: missing prompt text")
    sys.exit(2)

# Send prompt
client = genai.Client(api_key=api_key)
text = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt)
    )
if text.usage_metadata is None:
    raise RuntimeError("API request failed")

# debug & to check token usage (for API limits)
if args.verbose:
    print(f"User prompt: {args.user_prompt}\nPrompt tokens: {text.usage_metadata.prompt_token_count}\nResponse tokens: {text.usage_metadata.candidates_token_count}")

print(text.text)

