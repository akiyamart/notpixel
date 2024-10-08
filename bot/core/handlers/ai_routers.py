from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.fsm.context import FSMContext
from datetime import datetime

from ..tools.decorators import db_session_decorator
from ..settings import bot
from ..states import AIConnect
from ..chatGPT import chat_gpt_session
from ..ui import menu, back_to_menu


router = Router()


@router.message(F.data == "chat_ai")
async def start_handler(callback_query: CallbackQuery, db: AsyncSession):
    await callback_query.message.answer(
            text=f"Попробуй задать вопрос 🤓",
            reply_markup=back_to_menu()
    )

@router.message(AIConnect.gpt_state)
@db_session_decorator
async def AI_assistant_text_handler(message: Message, state: FSMContext, ):
    data = await state.get_data()
    history = data.get("history", [])
    
    await bot.send_chat_action(message.chat.id, action="typing")
