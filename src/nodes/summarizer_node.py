import os
from langchain_openai import ChatOpenAI
from src.agent.state import AgentState

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


def summarizer_node(state: AgentState) -> AgentState:
    """
    Summarize the financial information of a stock ticker.

    Args:
        state (AgentState): The current state containing the ticker and its information.
        llm (ChatOpenAI): The language model to use for summarization.

    Returns:
        AgentState: The updated state with the summary included.
    """
    if not state.get("ticker_info"):
        state["summary"] = "No ticker information available to summarize."
        return state
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini", api_key=OPENAI_API_KEY)
    prompt = f"Summarize the following financial information about {state['ticker']}:\n{state['ticker_info']}"

    response = llm.invoke([{"role": "user", "content": prompt}])
    state["summary"] = response.content
    return state
