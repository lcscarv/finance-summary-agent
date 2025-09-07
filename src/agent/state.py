from typing import Optional, TypedDict
from langchain_core.messages import HumanMessage


class AgentState(TypedDict):
    user_message: Optional[HumanMessage]
    ticker: Optional[str]
    requested_info: Optional[list[str]]
    ticker_info: Optional[dict]
    summary: Optional[str]
