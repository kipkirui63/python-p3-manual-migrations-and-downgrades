"""Rename column

Revision ID: 4688419e699c
Revises: 9bd5c218f483
Create Date: 2023-09-01 08:47:15.662121

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4688419e699c'
down_revision: Union[str, None] = '9bd5c218f483'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
