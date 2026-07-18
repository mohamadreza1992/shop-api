"""add user role"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "1a94dd2bc811"
down_revision: Union[str, Sequence[str], None] = "69611553ec8e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    user_role = sa.Enum("user", "admin", name="user_role")
    user_role.create(op.get_bind(), checkfirst=True)

    op.add_column(
        "users",
        sa.Column(
            "role",
            user_role,
            nullable=False,
            server_default="user",
        ),
    )

    op.alter_column(
        "users",
        "role",
        server_default=None,
    )


def downgrade() -> None:
    op.drop_column("users")

    user_role = sa.Enum("user", "admin", name="user_role")
    user_role.drop(op.get_bind(), checkfirst=True)