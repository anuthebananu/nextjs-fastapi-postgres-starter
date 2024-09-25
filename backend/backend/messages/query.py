from typing import Optional
from uuid import UUID, uuid4
from models import Content, Conversation, Message
from sqlalchemy.ext.asyncio import AsyncSession
from db_engine import engine

class MessagesQuery:
    def __init__(self, session: AsyncSession):
         self.session = session

    async def get_messages_for_conversation(self, conversation_id: UUID):
            # TODO don't create a new session every time, use a shared session
            # throughout the app
            return self.session.get(Message, {"conversation_id": conversation_id})
    
    async def create_conversation(self, user_id: int) -> Conversation:
            conversation = Conversation(id=uuid4(), owner_id=user_id)
            self.session.add(conversation)
            return conversation
    
    async def create_message_content(self, text: str):
            content = Content(id=uuid4(), text=text)
            self.session.add(content)
            return content
    
    async def get_or_create_conversation(self, user_id: UUID, conversation_id: Optional[UUID]):
            if conversation_id:
                return self.session.get(Conversation, conversation_id)
            else:
                return await self.create_conversation(user_id)
                