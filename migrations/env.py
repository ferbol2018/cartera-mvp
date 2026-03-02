from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Importa tu Base y DATABASE_URL desde config.py
from app.core.config import DATABASE_URL, Base

# Configuración de logging
config = context.config
fileConfig(config.config_file_name)

# Metadata de tus modelos
target_metadata = Base.metadata


def run_migrations_offline():
    """Ejecuta migraciones en modo offline (sin conexión directa)."""
    url = DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Ejecuta migraciones en modo online (con conexión real)."""
    connectable = engine_from_config(
        {"sqlalchemy.url": DATABASE_URL},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # detecta cambios en tipos de columnas
        )

        with context.begin_transaction():
            context.run_migrations()


# Decide si correr offline u online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()