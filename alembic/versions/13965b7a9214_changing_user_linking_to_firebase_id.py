"""changing user linking to firebase id

Revision ID: 13965b7a9214
Revises: e2fcea6e7682
Create Date: 2022-07-10 19:44:35.517373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13965b7a9214'
down_revision = 'e2fcea6e7682'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('firebase_id', sa.String(length=255), nullable=True))
    op.drop_constraint('games_user_id_fkey', 'games', type_='foreignkey')
    op.create_foreign_key(None, 'games', 'users', ['firebase_id'], ['firebase_id'])
    op.drop_column('games', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'games', type_='foreignkey')
    op.create_foreign_key('games_user_id_fkey', 'games', 'users', ['user_id'], ['id'])
    op.drop_column('games', 'firebase_id')
    # ### end Alembic commands ###
