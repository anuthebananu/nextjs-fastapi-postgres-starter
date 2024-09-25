from uuid import UUID
from backend.messages.processing import process_create_message_request
from backend.messages.schema import CreateMessageRequest
import backend.messages.query as MessagesQuery
from fastapi import APIRouter, BackgroundTasks, status
from models import Conversation

messages_router = APIRouter()

@messages_router.post("/messages", status_code=status.HTTP_202_ACCEPTED)
async def send_message(request: CreateMessageRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_create_message_request, request=request)
    return "Accepted the message"


@messages_router.get("/messages")
async def get_conversation_messages(conversation_id: UUID):
    return MessagesQuery.getConversationMessages(conversation_id=conversation_id)
