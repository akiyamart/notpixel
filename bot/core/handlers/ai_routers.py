from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.fsm.context import FSMContext
from datetime import datetime

from ..states import AIConnect
from ..chatGPT import chat_gpt_session
from ..ui import back_to_menu, clear_data

router = Router()

@router.callback_query(F.data == "chat_ai")
async def start_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(AIConnect.gpt_state)
    await callback_query.answer()
    await callback_query.message.answer(
        text="Попробуй задать вопрос 🤓",
        reply_markup=back_to_menu()
    )

@router.callback_query(F.data == "clear_data")
async def start_handler(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await state.set_data({})
    await callback_query.message.answer(
        text="Память была очищена 🗑"
    )
    
@router.message(AIConnect.gpt_state)
async def AI_assistant_text_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    history = data.get("history", [])
    print("history", history)

    input_reply_data = ""
    if message.reply_to_message: 
        input_reply_data = message.reply_to_message.text

    user_data = (
        f"Сообщение от пользователя: {message.text}\nReply data: {input_reply_data}\n" 
    )
    user_data_for_gpt = (
        user_data + f"История сообщений: {history}"
    )
    
    if not isinstance(history, list):
        history = []
        
    history.append({"role": "user", "content": user_data_for_gpt})
    await state.set_data({"history": history})

    response = await chat_gpt_session.chat_gpt_session_text(messages=history)
    raw_content = response['choices'][0]['message']['content']

    await message.answer(
        text=f"{raw_content}", 
        reply_markup=clear_data()
    )
