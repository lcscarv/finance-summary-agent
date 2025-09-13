from langgraph.graph import START, END, StateGraph
from src.agent.state import AgentState
from src.nodes.finance_nodes import (
    fetch_ticker_node,
    fetch_recommendations_node,
    fetch_fundamentals_node,
    fetch_news_node,
)
from src.nodes.intent_node import intent_node
from src.nodes.general_chat_node import general_chat_node
from src.nodes.summarizer_node import summarizer_node


def intent_router(state: AgentState) -> str:
    if "general_chat" in state["requested_info"]:
        return "general"
    return "finance"


workflow = StateGraph(state_schema=AgentState)

workflow.add_node("intent", intent_node)
workflow.add_node("fetch_ticker", fetch_ticker_node)
workflow.add_node("fetch_recommendations", fetch_recommendations_node)
workflow.add_node("fetch_fundamentals", fetch_fundamentals_node)
workflow.add_node("fetch_news", fetch_news_node)
workflow.add_node("summarize", summarizer_node)
workflow.add_node("general_chat", general_chat_node)

workflow.add_edge(START, "intent")
workflow.add_conditional_edges(
    "intent", intent_router, {"finance": "fetch_ticker", "general": "general_chat"}
)
workflow.add_edge("fetch_ticker", "fetch_recommendations")
workflow.add_edge("fetch_recommendations", "fetch_fundamentals")
workflow.add_edge("fetch_fundamentals", "fetch_news")
workflow.add_edge("fetch_news", "summarize")
workflow.add_edge("summarize", END)

workflow.add_edge("general_chat", END)
graph = workflow.compile()
