"""add last few solumns to posts table

Revision ID: 801b66d57e7b
Revises: 4c09b947fd7d
Create Date: 2023-05-26 15:18:49.132991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '801b66d57e7b'
down_revision = '4c09b947fd7d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')    
    op.drop_column('posts', 'created_at')
  
    pass
