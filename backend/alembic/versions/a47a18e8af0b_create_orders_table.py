"""create orders table

Revision ID: a47a18e8af0b
Revises: 
Create Date: 2025-09-06 05:05:20.687321

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a47a18e8af0b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column('full_name', sa.String(), nullable=False),
        sa.Column('phone', sa.String(255), nullable=False),
        sa.Column('tg_username', sa.String(255), nullable=True),
        sa.Column('address_line', sa.String(), nullable=False),
        sa.Column('city', sa.String(), nullable=False),
        sa.Column('postal_code', sa.String(), nullable=True),
        sa.Column('region', sa.String(), nullable=False, server_default="Andijon"),
        sa.Column('status', sa.String(), nullable=False, server_default="pending"),
        sa.Column('total_amount', sa.Float(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), onupdate=sa.func.now())
    )



def downgrade() -> None:
    pass
