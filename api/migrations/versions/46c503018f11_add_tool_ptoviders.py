"""add tool ptoviders

Revision ID: 46c503018f11
Revises: 2beac44e5f5f
Create Date: 2023-07-07 16:35:32.974075

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '46c503018f11'
down_revision = '2beac44e5f5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tool_providers',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('tenant_id', postgresql.UUID(), nullable=False),
    sa.Column('tool_name', sa.String(length=40), nullable=False),
    sa.Column('encrypted_config', sa.Text(), nullable=True),
    sa.Column('is_valid', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.PrimaryKeyConstraint('id', name='tool_provider_pkey'),
    sa.UniqueConstraint('tenant_id', 'tool_name', name='unique_tool_provider_tool_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tool_providers')
    # ### end Alembic commands ###
