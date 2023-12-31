"""empty message

Revision ID: 89bf5cb8e2e9
Revises: 
Create Date: 2023-10-30 14:14:39.524558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89bf5cb8e2e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('token')
    )
    op.create_table('books',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('author', sa.String(length=150), nullable=False),
    sa.Column('genre', sa.String(length=150), nullable=False),
    sa.Column('isbn', sa.String(length=150), nullable=False),
    sa.Column('hardcover', sa.Boolean(), nullable=False),
    sa.Column('length', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.drop_table('user')
    # ### end Alembic commands ###
