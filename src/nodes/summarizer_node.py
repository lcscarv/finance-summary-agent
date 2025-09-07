from langchain_openai import ChatOpenAI
from src.agent.state import AgentState


def summarizer_node(state: AgentState, llm: ChatOpenAI) -> AgentState:
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
    prompt = f"Summarize the following financial information about {state['ticker']}:\n{state['ticker_info']}"

    response = llm.invoke([{"role": "user", "content": prompt}])
    return AgentState(**{**state, "summary": response.content})
