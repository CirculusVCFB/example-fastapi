"""create alembic table

Revision ID: c8915990fff5
Revises: 
Create Date: 2022-01-19 16:35:55.314249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8915990fff5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("alembic", sa.Column('id', sa.Integer(), nullable = False, primary_key=True),
    sa.Column('title', sa.String(1000), nullable = False))
    pass


def downgrade():
    op.drop_table("posts")
    pass
