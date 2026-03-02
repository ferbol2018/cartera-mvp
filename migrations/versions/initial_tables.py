"""Initial tables

Revision ID: 0001_initial
Revises: 
Create Date: 2026-03-02 11:30:00

"""
from alembic import op
import sqlalchemy as sa


# Identificadores de migración
revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Tabla clients
    op.create_table(
        "clients",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("email", sa.String, unique=True, index=True),
    )

    # Tabla invoices
    op.create_table(
        "invoices",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("client_id", sa.Integer, sa.ForeignKey("clients.id"), nullable=False),
        sa.Column("amount", sa.Integer, nullable=False),
        sa.Column("status", sa.String, default="pending"),
        sa.Column("due_date", sa.Date),
    )

    # Tabla payments
    op.create_table(
        "payments",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("invoice_id", sa.Integer, sa.ForeignKey("invoices.id"), nullable=False),
        sa.Column("amount", sa.Integer, nullable=False),
        sa.Column("payment_date", sa.Date),
    )


def downgrade():
    op.drop_table("payments")
    op.drop_table("invoices")
    op.drop_table("clients")