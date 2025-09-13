from typing import Optional, TypedDict
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI


class AgentState(TypedDict):
    user_message: HumanMessage
    llm: ChatOpenAI
    ticker: Optional[str]
    requested_info: Optional[list[str]]
    ticker_info: Optional[dict]
    summary: Optional[str]
    general_response: Optional[str]
