from langchain_core.messages import HumanMessage
from langchain_openai.chat_models import ChatOpenAI
from pydantic import BaseModel, Field

from src.agent.state import AgentState


class IntentOutput(BaseModel):
    ticker: str = Field(
        ..., description="The stock ticker symbol, e.g., AAPL for Apple Inc."
    )
    info_requested: list[str] = Field(
        ...,
        description=(
            "List of information types requested by the user. "
            'Possible values include "price", "news", "fundamentals", "recommendations", or "all".'
        ),
    )


def intent_node(
    user_input: HumanMessage, llm: ChatOpenAI, state: AgentState
) -> AgentState:
    """
    Determine the user's intent from their input message.

    Args:
        user_input (HumanMessage): The user's input message.
        llm (ChatOpenAI): The language model to use for intent determination.

    Returns:
        str: The determined intent as a string.
    """
    llm_structured = llm.with_structured_output(IntentOutput)

    prompt = f"""Given the following user message, 
    extract the ticker symbol and what information they want 
    (price, news, fundamentals, recommendations). If no clear direction of what
    info the user wants, you must use every information: f{user_input.content}"""

    response: IntentOutput = llm_structured.invoke(
        [{"role": "user", "content": prompt}]
    )  # type: ignore

    state["ticker"] = response.ticker
    state["requested_info"] = response.info_requested
    return state
