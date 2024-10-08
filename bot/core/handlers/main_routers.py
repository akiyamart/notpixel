from aiogram import Router, F 
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from ..tools.decorators import db_session_decorator
from ..ui import menu, back_to_menu

router = Router()

# @db_session_decorator

@router.message(Command("start"))
async def start_handler(message: Message,):
    await message.answer(
            text=f"Привет, {message.from_user.username}, выбери, что ты хочешь сделать 🤔",
            reply_markup=menu()
        )

@router.message(F.data == "menu")
async def start_handler(callback_query: CallbackQuery, db: AsyncSession):
    await callback_query.message.answer(
            text=f"Выбери действие нижe 👇",
            reply_markup=menu()
    )