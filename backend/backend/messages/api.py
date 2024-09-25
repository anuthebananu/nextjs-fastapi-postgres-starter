from uuid import UUID
from backend.messages.schema import CreateMessageRequest
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from db_engine import engine

messages_router = APIRouter()

@messages_router.post("/messages", status_code=201)
async def send_message(message: CreateMessageRequest):
    async with AsyncSession(engine) as session:
        async with session.begin():
            # send to message processor
            print("message: {message}")
            print("Sending to message processor")

@messages_router.get("/messages")
async def get_conversation_messages(conversation_id: int):
    return "These are your messages"
