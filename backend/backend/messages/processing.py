from datetime import datetime
from uuid import uuid4
from backend.messages.schema import CreateMessageRequest
from models import Content, Conversation, Message
from sqlalchemy.ext.asyncio import AsyncSession
from db_engine import engine
import logging
from backend.messages.query import MessagesQuery

logger = logging.getLogger(__name__)


async def process_create_message_request(request: CreateMessageRequest):
    async with AsyncSession(engine) as session:
        async with session.begin():
            messages_query_processor = MessagesQuery(session=session)

            conversation = await messages_query_processor.get_or_create_conversation(user_id=request.user_id, conversation_id=request.conversation_id)

            content = await messages_query_processor.create_message_content(request.text)

            message = Message(
                    id=uuid4(),
                    received_at=datetime.now(),
                    sender_id=request.user_id,
                    content_id=content.id,
                    conversation_id=conversation.id,
                    status="PROCESSING"
            )
            session.add(message)
            
            await session.commit()
        

        