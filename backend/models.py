from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String
from uuid import UUID, uuid4
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}"

class Content(Base):
    __tablename__ = "contents"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4())
    text: Mapped[str] = mapped_column(String)

    def __repr__(self) -> str:
        return f"Content(id={self.id!r}, text={self.text!r})"

class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4())
    owner_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def __repr__(self) -> str:
        return f"Conversation(id={self.id!r}, owner_id={self.owner_id!r})"

class Response(Base):
    __tablename__ = "responses"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4())
    sent_at: Mapped[datetime] = mapped_column(DateTime)
    content_id: Mapped[UUID] = mapped_column(ForeignKey("contents.id"))

class Message(Base):
    __tablename__ = "messages"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4())
    received_at: Mapped[datetime] = mapped_column(DateTime)
    processed_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    status: Mapped[str] = mapped_column(String)
    sender_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    content_id: Mapped[UUID] = mapped_column(ForeignKey("contents.id"))
    conversation_id: Mapped[UUID] = mapped_column(ForeignKey("conversations.id"))


