from src.agent.state import AgentState


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
        state["response"] = "No ticker information available to summarize."
        return state
    llm = state["llm"]
    prompt = f"Summarize the following financial information about {state['ticker']}:\n{state['ticker_info']}"

    response = llm.invoke([{"role": "user", "content": prompt}])
    state["response"] = response.content
    return state
