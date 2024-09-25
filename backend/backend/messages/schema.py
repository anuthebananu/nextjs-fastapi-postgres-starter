from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

class CreateMessageRequest(BaseModel):
    user_id: int
    text: str
    conversation_id: Optional[UUID] = None

# Can be augmented in future w/ image url, video url, metadata, etc
class ContentResponse(BaseModel):
    id: UUID
    text: str

class MessageResponse(BaseModel):
    id: UUID
    receivedAt: datetime
    processedAt: datetime
    status: str
    sender_id: int
    content: ContentResponse
    conversation_id: UUID

# TODO pagination
class MessagesResponse(BaseModel):
    data: list[MessageResponse]

