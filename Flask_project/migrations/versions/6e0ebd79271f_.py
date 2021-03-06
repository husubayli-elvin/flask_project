"""empty message

Revision ID: 6e0ebd79271f
Revises: da73f02eb0e6
Create Date: 2020-10-22 23:55:44.009759

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6e0ebd79271f'
down_revision = 'da73f02eb0e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'book_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.create_index(op.f('ix_comment_book_id'), 'comment', ['book_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comment_book_id'), table_name='comment')
    op.alter_column('comment', 'book_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
