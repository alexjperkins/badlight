"""empty message

Revision ID: d930bb9eb392
Revises: 263af6259450
Create Date: 2020-05-01 08:31:33.912128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd930bb9eb392'
down_revision = '263af6259450'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', '_password',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', '_password',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    # ### end Alembic commands ###
