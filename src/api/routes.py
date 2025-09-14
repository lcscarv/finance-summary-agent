import uuid
from fastapi import APIRouter
from langchain_core.messages import HumanMessage
from src.api.models import ChatRequest, ChatResponse
from src.agent.finance_agent import FinanceAgent

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest) -> dict:
    if not req.session_id:
        req.session_id = str(uuid.uuid4())

    user_message = req.message
    human_message = HumanMessage(content=user_message)
    agent = FinanceAgent(human_message)
    final_state = agent.run()

    return {"response": final_state.get("response"), "session_id": req.session_id}
