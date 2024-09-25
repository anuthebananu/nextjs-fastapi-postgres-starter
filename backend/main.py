from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from seed import seed_user_if_needed
from sqlalchemy.ext.asyncio import AsyncSession
from db_engine import engine
from models import User
from backend.users.api import users_router
from backend.messages.api import messages_router

seed_user_if_needed()

app = FastAPI()

app.include_router(users_router)
app.include_router(messages_router)