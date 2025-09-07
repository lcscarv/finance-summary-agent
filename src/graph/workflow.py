from langgraph.graph import START, END, StateGraph
from src.agent.state import AgentState
from src.nodes.finance_nodes import (
    fetch_ticker_node,
    fetch_recommendations_node,
    fetch_fundamentals_node,
    fetch_news_node,
)
from src.nodes.intent_node import intent_node
from src.nodes.summarizer_node import summarizer_node


workflow = StateGraph(state_schema=AgentState)

workflow.add_node("intent", intent_node)
workflow.add_node("fetch_ticker", fetch_ticker_node)
workflow.add_node("fetch_recommendations", fetch_recommendations_node)
workflow.add_node("fetch_fundamentals", fetch_fundamentals_node)
workflow.add_node("fetch_news", fetch_news_node)
workflow.add_node("summarize", summarizer_node)

workflow.add_edge(START, "intent")
workflow.add_edge("intent", "fetch_ticker")
workflow.add_edge("fetch_ticker", "fetch_recommendations")
workflow.add_edge("fetch_recommendations", "fetch_fundamentals")
workflow.add_edge("fetch_fundamentals", "fetch_news")
workflow.add_edge("fetch_news", "summarize")
workflow.add_edge("summarize", END)

graph = workflow.compile()
