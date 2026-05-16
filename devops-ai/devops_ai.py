import os
from dotenv import load_dotenv
from google import genai
import argparse

load_dotenv()
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
    response = client.models.generate_content(
        model = 'gemini-2.5-flash-lite' ,
        contents = prompt
    )
    return response.text.strip()

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

