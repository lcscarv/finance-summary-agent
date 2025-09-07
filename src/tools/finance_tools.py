import json
import yfinance as yf
from langchain.tools import tool


@tool
def get_current_stock_price(ticker: str) -> float | str:
    """
    Get the current stock price for a given ticker symbol.

    Args:
        ticker (str): The ticker symbol of the stock.

    Returns:
        float: The current stock price.
    """
    stock = yf.Ticker(ticker)
    current_price = stock.info.get("regularMarketPrice", stock.info.get("currentPrice"))

    return (
        f"{current_price:.2f}"
        if current_price
        else f"Could not fetch price for {ticker}"
    )


@tool
def get_analyst_recommendations(ticker: str) -> str:
    """
    Get the latest analyst recommendations for a given ticker symbol.

    Args:
        ticker (str): The ticker symbol of the stock.

    Returns:
        str: A summary of the latest analyst recommendations.
    """
    try:
        stock = yf.Ticker(ticker)
        recommendations = stock.recommendations
        return recommendations.to_json(orient="index")
    except Exception as e:
        return f"Could not fetch recommendations for {ticker}: {str(e)}"


@tool
def get_stock_fundamentals(ticker: str) -> str:
    """
    Get the stock fundamentals for a given ticker symbol.

    Returns:
        str: A JSON string containing key stock fundamentals.
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        fundamentals = {
            "symbol": ticker,
            "company_name": info.get("LongName", ""),
            "sector": info.get("sector", ""),
            "industry": info.get("industry", ""),
            "market_cap": info.get("marketCap"),
            "trailingPE": info.get("trailingPE"),
            "forwardPE": info.get("forwardPE"),
            "priceToBook": info.get("priceToBook"),
            "dividendYield": info.get("dividendYield"),
            "beta": info.get("beta"),
            "fiftyTwoWeekHigh": info.get("fiftyTwoWeekHigh"),
            "fiftyTwoWeekLow": info.get("fiftyTwoWeekLow"),
        }
        return json.dumps(fundamentals)
    except Exception as e:
        return f"Could not fetch fundamentals for {ticker}: {str(e)}"


@tool
def get_company_news(ticker: str, num_stories: int = 3) -> str:
    """Use this function to get company news and press releases for a given stock symbol.

    Args:
        symbol (str): The stock symbol.
        num_stories (int): The number of news stories to return. Defaults to 3.

    Returns:
        str: JSON containing company news and press releases.
    """
    try:
        stock = yf.Ticker(ticker)
        news = stock.news
        return json.dumps(news[:num_stories], indent=2)
    except Exception as e:
        return f"Could not fetch news for {ticker}: {str(e)}"
