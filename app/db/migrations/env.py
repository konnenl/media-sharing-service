from app.db.database import Base
from app.models import *
from alembic import context
from app.core.config import SYNC_DATABASE_URL

config = context.config
config.set_main_option(
    "sqlalchemy.url",
    SYNC_DATABASE_URL
)
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    from app.db.database import sync_engine
    from sqlalchemy import create_engine
    
    connectable = sync_engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()