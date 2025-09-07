import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from src.agent.state import AgentState
from src.graph.workflow import graph

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


class FinanceAgent:
    def __init__(self, user_message: HumanMessage):
        self.user_message = user_message
        self.llm = ChatOpenAI(
            temperature=0, model="gpt-4o-mini", api_key=OPENAI_API_KEY
        )

    def run(self) -> AgentState:
        state: AgentState = {
            "user_message": self.user_message,
            "llm": self.llm,
            "ticker": "",
            "requested_info": [],
            "ticker_info": {},
            "summary": None,
        }
        for event in graph.stream(state):
            print(f"Node: {event}")

        final_state = graph.invoke(state)
        return final_state

    def get_summary(self) -> AgentState:
        state = self.run()
        return state
