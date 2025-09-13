from langchain_core.messages import HumanMessage
from src.agent.finance_agent import FinanceAgent


def main():
    user_message = HumanMessage(content="What is the capital of Brazil?")
    agent = FinanceAgent(user_message)
    result = agent.run()
    if result["general_response"]:
        print(result["general_response"])
    print(result["summary"])


if __name__ == "__main__":
    main()
