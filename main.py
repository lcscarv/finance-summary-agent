from langchain_core.messages import HumanMessage
from src.agent.finance_agent import FinanceAgent


def main():
    user_message = HumanMessage(
        content="What is the current available stock price and recommendations for AAPL?"
    )
    agent = FinanceAgent(user_message)
    result = agent.run()
    print(result["summary"])


if __name__ == "__main__":
    main()
