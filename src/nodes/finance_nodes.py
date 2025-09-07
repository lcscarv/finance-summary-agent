from src.agent.state import AgentState
from src.tools.finance_tools import (
    get_current_stock_price,
    get_analyst_recommendations,
    get_stock_fundamentals,
    get_company_news,
)


def fetch_ticker_node(state: AgentState) -> AgentState:
    """
    Fetch basic information about a stock ticker.

    Args:
        ticker (str): The ticker symbol of the stock.

    Returns:
        dict | str: A dictionary containing key stock fundamentals or an error message.
    """
    if "price" not in state.get("requested_info", []):
        return state
    ticker = state["ticker"]
    stock_price_info = get_current_stock_price(ticker)
    ticker_info = state.get("ticker_info", {})
    ticker_info["current_price"] = stock_price_info
    return AgentState(**{**state, "ticker": ticker, "ticker_info": ticker_info})


def fetch_recommendations_node(state: AgentState) -> AgentState:
    """
    Fetch analyst recommendations for a stock ticker.

    Args:
        ticker (str): The ticker symbol of the stock.

    Returns:
        dict | str: A JSON string containing analyst recommendations or an error message.
    """
    if "recommendations" not in state.get("requested_info", []):
        return state
    ticker = state["ticker"]
    stock_recommendations = get_analyst_recommendations(ticker)
    ticker_info = state.get("ticker_info", {})
    ticker_info["recommendations"] = stock_recommendations
    return AgentState(**{**state, "ticker": ticker, "ticker_info": ticker_info})


def fetch_fundamentals_node(state: AgentState) -> AgentState:
    """
    Fetch stock fundamentals for a stock ticker.

    Args:
        ticker (str): The ticker symbol of the stock.

    Returns:
        dict | str: A JSON string containing key stock fundamentals or an error message.
    """
    if "fundamentals" not in state.get("requested_info", []):
        return state
    ticker = state["ticker"]
    stock_fundamentals = get_stock_fundamentals(ticker)
    ticker_info = state.get("ticker_info", {})
    ticker_info["fundamentals"] = stock_fundamentals
    return AgentState(**{**state, "ticker": ticker, "ticker_info": ticker_info})


def fetch_news_node(state: AgentState) -> AgentState:
    """
    Fetch recent news articles for a stock ticker.

    Args:
        ticker (str): The ticker symbol of the stock.

    Returns:
        dict | str: A JSON string containing recent news articles or an error message.
    """
    if "news" not in state.get("requested_info", []):
        return state
    ticker = state["ticker"]
    stock_news = get_company_news(ticker)
    ticker_info = state.get("ticker_info", {})
    ticker_info["news"] = stock_news
    return AgentState(**{**state, "ticker": ticker, "ticker_info": ticker_info})
