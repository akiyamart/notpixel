from aiogram import Dispatcher

from ..handlers import (main_router)

def dp_setting(dp: Dispatcher) -> None: 
    dp.include_router(main_router)