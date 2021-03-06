"""empty message

Revision ID: 109bbe01496b
Revises: 
Create Date: 2018-06-10 04:18:28.701583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '109bbe01496b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('professor_name', sa.String(length=1000), nullable=True),
    sa.Column('email', sa.String(length=1000), nullable=True),
    sa.Column('project_description', sa.String(length=1000), nullable=True),
    sa.Column('key_words', sa.String(length=1000), nullable=True),
    sa.Column('project_title', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    # ### end Alembic commands ###
