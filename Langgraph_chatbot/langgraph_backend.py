from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import os 

from pathlib import Path

# Always load .env from project root (Langgraph/)
ROOT_DIR = Path(__file__).resolve().parents[1]  # go 1 level up from Chatbot/
load_dotenv(override=True,dotenv_path=ROOT_DIR / ".env")

openai_api_key = os.getenv("OPENAI_API_KEY")

try :
    llm = ChatOpenAI(model='gpt-4o-mini', temperature=0, api_key=openai_api_key)

    class ChatState(TypedDict):
        messages: Annotated[list[BaseMessage], add_messages]

    def chat_node(state: ChatState):
        messages = state['messages']
        response = llm.invoke(messages)
        return {"messages": [response]}

    # Checkpointer
    checkpointer = InMemorySaver()

    graph = StateGraph(ChatState)
    graph.add_node("chat_node", chat_node)
    graph.add_edge(START, "chat_node")
    graph.add_edge("chat_node", END)

    chatbot = graph.compile(checkpointer=checkpointer)

except Exception as e:
    print(e)
