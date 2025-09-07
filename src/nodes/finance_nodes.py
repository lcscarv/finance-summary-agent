from src.tools.finance_tools import get_current_stock_price
from src.agent.state import AgentState


def fetch_ticker_node(state: AgentState, ticker: str) -> AgentState:
    """
    Fetch basic information about a stock ticker.

    Args:
        ticker (str): The ticker symbol of the stock.

    Returns:
        dict | str: A dictionary containing key stock fundamentals or an error message.
    """
    stock_info = get_current_stock_price(ticker)
    return AgentState(**{**state, "ticker": ticker, "ticker_info": stock_info})
