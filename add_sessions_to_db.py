import os
import asyncio
from sqlalchemy.orm import Session as AsyncSession

from bot.core.database.models import Session
from sqlalchemy.future import select
from bot.core.tools.decorators import db_session_decorator

@db_session_decorator
async def add_sessions(session_names, db: AsyncSession):
    for name in session_names:
        stmt = select(Session).where(Session.session_name == name)
        result = await db.execute(stmt)
        existing_session = result.scalars().first()

        if existing_session is None:
            new_session = Session(session_name=name)
            db.add(new_session)
            print(f"Добавлена сессия: {name}")

    await db.commit()
    print("Все сессии добавлены и изменения сохранены в базе данных.")

if __name__ == "__main__":
    session_names = os.listdir('./sessions')
    asyncio.run(
        add_sessions(session_names)
    )
