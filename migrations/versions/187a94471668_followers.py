"""followers

Revision ID: 187a94471668
Revises: 16e3bd4ade91
Create Date: 2018-11-22 10:42:17.265681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '187a94471668'
down_revision = '16e3bd4ade91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
