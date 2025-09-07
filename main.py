from src.agent.finance_agent import FinanceAgent


def main():
    agent = FinanceAgent("AAPL")
    result = agent.run()
    print(result["summary"])


if __name__ == "__main__":
    main()
