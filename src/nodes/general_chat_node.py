from src.agent.state import AgentState


def general_chat_node(state: AgentState):
    llm = state["llm"]
    user_input = state["user_message"]
    response = llm.invoke([{"role": "user", "content": user_input.content}])
    state["general_response"] = response.content
    return state
