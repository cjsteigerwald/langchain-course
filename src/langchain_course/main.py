import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

def main() -> None:
    print("Hello from langchain-course!")

if __name__ == "__main__":
    main()