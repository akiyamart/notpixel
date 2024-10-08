from aiogram.fsm.state import StatesGroup, State

class AIConnect(StatesGroup): 
    gpt_state = State()
    whisper_state = State()
