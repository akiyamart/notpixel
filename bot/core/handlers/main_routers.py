from aiogram import Router, F 
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from ..tools.decorators import db_session_decorator

router = Router()

@router.message(Command("start"))
@db_session_decorator
async def start_handler(message: Message, db: AsyncSession):
    await message.answer(
            text=f"Привет, {message.from_user.username}",
        )