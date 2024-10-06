"""create sessions table

Revision ID: 97804ef18510
Revises: 
Create Date: 2024-10-06 14:26:36.909961

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid



# revision identifiers, used by Alembic.
revision: str = '97804ef18510'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Создание таблицы sessions
    op.create_table(
        'sessions',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('session_name', sa.Text, nullable=True),
        sa.Column('proxy_text', sa.Text, nullable=True)
    )

def downgrade():
    # Удаление таблицы sessions
    op.drop_table('sessions')