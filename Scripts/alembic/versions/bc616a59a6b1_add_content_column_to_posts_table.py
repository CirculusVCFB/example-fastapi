"""add content column to posts table

Revision ID: bc616a59a6b1
Revises: c8915990fff5
Create Date: 2022-01-20 00:51:50.206142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc616a59a6b1'
down_revision = 'c8915990fff5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("contents", sa.String(1000), nullable = False))
    pass


def downgrade():
    op.drop_column('posts', 'contents')
    pass
