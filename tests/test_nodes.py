import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from src.nodes.intent_node import intent_node
from src.agent.state import AgentState

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini", api_key=OPENAI_API_KEY)


def test_intent_node():
    user_input = HumanMessage(content="What is the capital of Brazil?")
    state = AgentState(
        user_message=user_input,
        llm=llm,
        ticker=None,
        requested_info=None,
        ticker_info={},
        response=None,
    )
    final_state = intent_node(state)
    info_requested = final_state.get("requested_info", [])
    assert final_state["ticker"] == "AAPL"
    assert "price" in info_requested
    assert "news" in info_requested
