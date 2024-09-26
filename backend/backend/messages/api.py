from uuid import UUID
from backend.messages.processing import get_messages_for_conversation, process_create_message_request
from backend.messages.schema import CreateMessageRequest, MessageResponse, MessagesResponse
from fastapi import APIRouter, BackgroundTasks, status
from models import Conversation
from sqlalchemy.ext.asyncio import AsyncSession
from db_engine import engine

messages_router = APIRouter()

@messages_router.post("/messages", status_code=status.HTTP_202_ACCEPTED)
async def send_message(request: CreateMessageRequest, background_tasks: BackgroundTasks):
    async with AsyncSession(engine) as session:
        async with session.begin():
            background_tasks.add_task(process_create_message_request, session=session, request=request)
            return "Accepted the message"

# TODO implement
# @messages_router.post("/conversation", status_code=status.HTTP_201_CREATED)
# async def create_conversation(request: CreateConversationRequest):
#     # create a conversation

@messages_router.get("/messages")
async def list_messages(conversation_id: UUID):
    async with AsyncSession(engine) as session:
        async with session.begin():
            messages = await get_messages_for_conversation(conversation_id=conversation_id)
            for m in messages:
                m2 = await m
                print(m2)
            return MessagesResponse(data=[])
