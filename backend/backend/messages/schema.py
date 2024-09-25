from uuid import UUID
from pydantic import BaseModel

class CreateMessageRequest(BaseModel):
    conversation_id: UUID
    text: str
    