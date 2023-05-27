"""add content column to posts table

Revision ID: ca6b27fd96aa
Revises: 4a19bbb19270
Create Date: 2023-05-26 14:01:52.258881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca6b27fd96aa'
down_revision = '4a19bbb19270'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
