from typing import Optional, TypedDict


class AgentState(TypedDict):
    ticker: str
    ticker_info: Optional[dict]
    summary: Optional[str]
