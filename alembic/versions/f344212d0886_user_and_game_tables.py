"""user and game tables

Revision ID: f344212d0886
Revises: 
Create Date: 2022-06-15 23:34:33.368092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f344212d0886'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('frames', sa.String(length=63), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('firebase_id', sa.String(length=255), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.Column('has_input_frames', sa.Boolean(), nullable=True),
    sa.Column('total_score', sa.Integer(), nullable=True),
    sa.Column('total_games', sa.Integer(), nullable=True),
    sa.Column('total_strikes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('firebase_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('games')
    # ### end Alembic commands ###
