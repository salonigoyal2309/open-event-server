"""empty message

Revision ID: 0e80c49a6e28
Revises: b3bfa7949acf
Create Date: 2019-05-20 21:56:44.770504

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e80c49a6e28'
down_revision = 'b3bfa7949acf'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('is_ticket_form_enabled', sa.Boolean(), server_default='True', nullable=False))
    op.add_column('events_version', sa.Column('is_ticket_form_enabled', sa.Boolean(), server_default='True', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events_version', 'is_ticket_form_enabled')
    op.drop_column('events', 'is_ticket_form_enabled')
    # ### end Alembic commands ###