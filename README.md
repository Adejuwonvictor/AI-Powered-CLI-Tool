# devops-ai

An AI-powered command-line tool that converts plain English into Linux and DevOps shell commands.
Built with Python and the Google Gemini API.

---

## What It Does

- Converts plain English descriptions into shell commands
- Explains what any shell command does with the `--explain` flag
- Retries automatically on network failures
- AI model is configurable via a single config file

---

## Demo

```bash
$ python3 devops_ai.py "find all files larger than 100mb"
Command: find / -type f -size +100M

$ python3 devops_ai.py --explain "ps aux | grep python"
The ps aux command lists all currently running processes with details
like CPU and memory usage. The output is piped into grep which filters
and shows only lines containing the word python.
```

---

## Tech Stack

- Python 3
- Google Gemini API (`gemini-2.5-flash-lite`)
- `python-dotenv`
- `argparse`

---

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/Adejuwonvictor/AI-Powered-CLI-Tool
cd devops-ai
```

**2. Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your Gemini API key**

Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_key_here
```
Get a free key at [Google AI Studio](https://aistudio.google.com)

**5. Run the tool**
```bash
python3 devops_ai.py "your query here"
```

---

## Usage

**Generate a command:**
```bash
python3 devops_ai.py "list all running docker containers"
python3 devops_ai.py "show all open ports on this machine"
python3 devops_ai.py "find files modified in the last 24 hours"
```

**Explain a command:**
```bash
python3 devops_ai.py --explain "netstat -tulpn"
python3 devops_ai.py --explain "du -sh * | sort -rh"
```

**Change the AI model:**

Edit `config.py` and update the `model` field.

---

## Project Structure

```
devops-ai/
├── devops_ai.py      # Main CLI script
├── config.py         # Model and settings configuration
├── requirements.txt  # Python dependencies
├── .env              # API key (not committed to Git)
├── .gitignore        # Ignores .env and venv/
└── README.md         # This file
```

---

## Author

**Victor** — Junior DevOps Engineer  
[X](https://x.com/Vectorkole1)