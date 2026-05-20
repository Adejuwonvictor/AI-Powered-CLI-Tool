import os
import sys
import time
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import errors as genai_errors
from config import CONFIG

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    print('Error: GEMINI_API_KEY not found in environment variables.')
    sys.exit(1)
client = genai.Client()


COMMAND_PROMPT= """
You are a Linux and DevOps expert assistant.
When the user describes what they want to do, respond with ONLY the shell command that achieves it.
No explanation, no markdown, no backticks. Just the raw command.
Example:
User: show disk usage sorted by size
"""

EXPLAIN_PROMPT = """
You are a Linux and DevOps expert assistant.
When the user provides a shell command, explain clearly what it does in 2-4 sentences.
Break down each part of the command so a junior engineer can understand it.
No markdown formatting, just plain text.
"""
def ask_gemini(prompt):
    retries = 0
    while retries < CONFIG['max_retries']:
        try:
            response = client.models.generate_content(
                model = CONFIG['model'],
                contents = prompt
            )

            if not response.text or not response.text.strip():
                print('Received empty response from model. Retrying ...')
                retries+=1
                time.sleep(2)
                continue
            return response.text.strip()
    
        except genai_errors.APIError as e:
            print(f'API error: {e}')
            print('There is an issue with your API key or request. Please check your API key.\n')
            sys.exit(1)

        except Exception as e:
            retries+=1
            print(f'Unexpected error (attempt {retries}/{CONFIG["max_retries"]}): {e}. Retrying ...')
            if retries < CONFIG['max_retries']:
                print('Retrying in two seconds...')
                time.sleep(2)
            else:
                print('Max retries reached. Please check your API key and network connection.')
                sys.exit(1)
            
         

def explain_prompt(user_input):
    prompt = f"{EXPLAIN_PROMPT}\n\nUser input:{user_input} "
    return ask_gemini(prompt)

def get_command(command):
    prompt = f"{COMMAND_PROMPT}\n\nUser input:{command}"
    return ask_gemini(prompt)

def main():

    parser = argparse.ArgumentParser(description= "this is an input for the cli tool")
    parser.add_argument("query", type=str,
            help= "Describe what you want to do e.g. 'list all running docker containers'")
    parser.add_argument("--explain", action="store_true", 
            help="Explain what a command does instead of generating one")

    args = parser.parse_args()

    if args.explain:
        print(f'\nExplaining:{args.query}\n')
        Explanation = explain_prompt(args.query)
        print(f'{Explanation}\n')
    else:
        print(f'\nGenerating command for: {args.query}\n')
        Command = get_command(args.query)
        print(f'\nCommand: {Command}\n')

if __name__ == "__main__":
    main()

