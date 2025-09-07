import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from src.nodes.intent_node import intent_node
from src.agent.state import AgentState

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini", api_key=OPENAI_API_KEY)


def test_intent_node():
    user_input = HumanMessage(
        content="What is the current available information for AAPL?"
    )
    state = AgentState(
        user_message=user_input,
        ticker=None,
        requested_info=None,
        ticker_info={},
        summary=None,
    )
    result = intent_node(user_input, llm, state)
    info_requested = result.get("requested_info", [])
    assert result["ticker"] == "AAPL"
    assert "price" in info_requested
    assert "news" in info_requested
