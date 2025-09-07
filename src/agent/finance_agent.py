import os
from langchain_openai import ChatOpenAI

from src.agent.state import AgentState
from src.nodes.finance_nodes import fetch_ticker_node
from src.nodes.summarizer_node import summarizer_node

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


class FinanceAgent:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.llm = ChatOpenAI(
            temperature=0, model="gpt-4o-mini", api_key=OPENAI_API_KEY
        )

    def run(self) -> AgentState:
        state: AgentState = {
            "ticker": self.ticker,
            "ticker_info": None,
            "summary": None,
        }
        state = fetch_ticker_node(state, self.ticker)

        state = summarizer_node(state, self.llm)
        return state

    def get_summary(self) -> AgentState:
        state = self.run()
        return state
