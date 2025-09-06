"""create_orders_and_order_items_tables

Revision ID: ba3cadee7d24
Revises: a47a18e8af0b
Create Date: 2025-09-06 05:10:39.428623

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba3cadee7d24'
down_revision: Union[str, None] = 'a47a18e8af0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
