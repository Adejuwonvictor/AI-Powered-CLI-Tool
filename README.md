# devops-ai

A command-line tool that converts plain English into Linux/DevOps shell commands using AI.
Built with Python and the Google Gemini API.

## What it does

- Takes a plain English description and returns the correct shell command
- Can also explain what any shell command does
- Retries automatically on network failures
- Model is configurable via a single config file

## Demo

```bash
$ python3 devops_ai.py "find all files larger than 100mb"
Command: find / -type f -size +100M

$ python3 devops_ai.py --explain "ps aux | grep python"
The ps aux command lists all currently running processes with details like
CPU and memory usage. The output is piped into grep which filters and shows
only lines containing the word python, helping you find running Python processes.
```

## Tech Stack

- Python 3
- Google Gemini API (gemini-2.5-flash-lite)
- python-dotenv
- argparse

## Setup

1. Clone the repository
   git clone https://github.com/Adejuwonvictor/AI-Powered-CLI-Tool
   cd devops-ai

2. Create and activate a virtual environment
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install google-generativeai python-dotenv

4. Add your Gemini API key
   Create a .env file in the root directory:
   GEMINI_API_KEY=your_key_here

5. Run the tool
   python3 devops_ai.py "your query here"

## Usage

Generate a command:
   python3 devops_ai.py "list all running docker containers"

Explain a command:
   python3 devops_ai.py --explain "netstat -tulpn"

Change the AI model:
   Edit config.py and update the model field

## Project Structure

devops-ai/
├── devops_ai.py      # Main CLI script
├── config.py         # Model and settings configuration
├── .env              # API key (not committed to Git)
├── .gitignore        # Ignores .env and venv
└── README.md         # This file

## Author

Victor — Junior DevOps Engineer