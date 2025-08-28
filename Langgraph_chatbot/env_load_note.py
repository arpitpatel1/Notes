from dotenv import load_dotenv
import os
from pathlib import Path

# Detect project root (Langgraph/)
ROOT_DIR = Path(os.getcwd()).resolve()
if ROOT_DIR.name == "Chatbot":   # if you're inside subfolder
    ROOT_DIR = ROOT_DIR.parent   # go up one level

load_dotenv(override=True,dotenv_path=ROOT_DIR / ".env")

print("LangSmith Key:", os.getenv("LANGSMITH_API_KEY"))

# ------------------------------------------------------

from dotenv import load_dotenv
import os
from pathlib import Path

# Always load .env from project root (Langgraph/)
ROOT_DIR = Path(__file__).resolve().parents[1]  # go 1 level up from Chatbot/
load_dotenv(override=True,dotenv_path=ROOT_DIR / ".env")

# print(os.getenv("LANGSMITH_API_KEY"))
print("LangSmith Key:", os.getenv("OPENAI_API_KEY"))  # sanity check

