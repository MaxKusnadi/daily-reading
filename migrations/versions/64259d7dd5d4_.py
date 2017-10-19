"""empty message

Revision ID: 64259d7dd5d4
Revises: 
Create Date: 2017-10-19 11:56:41.334426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64259d7dd5d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reading',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('day', sa.Integer(), nullable=True),
    sa.Column('month', sa.Integer(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('result', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reading')
    # ### end Alembic commands ###