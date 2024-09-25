from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String
from uuid import UUID
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

class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    message_id: Mapped[UUID] = mapped_column(ForeignKey("messages.id"))

class Response(Base):
    __tablename__ = "responses"
    id: Mapped[UUID] = mapped_column(primary_key=True)
    sent_at: Mapped[datetime] = mapped_column(DateTime)
    content_id: Mapped[UUID] = mapped_column(ForeignKey("content.id"))

class Message(Base):
    __tablename__ = "messages"
    id: Mapped[UUID] = mapped_column(primary_key=True)
    received_at: Mapped[datetime] = mapped_column(DateTime)
    processed_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    status: Mapped[str] = mapped_column(String)
    sender_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    content_id: Mapped[UUID] = mapped_column(ForeignKey("content.id"))

class Content(Base):
    __tablename__ = "contents"
    id: Mapped[UUID] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String)

