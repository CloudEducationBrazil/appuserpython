import os

class Config:
    # Railway fornece DATABASE_URL (às vezes no formato postgres://)
    database_url = os.getenv(
        'DATABASE_URL',
        'postgresql+psycopg2://postgres:123456@localhost:5432/agendadb'
    )

    # Corrige prefixo "postgres://" (Railway usa isso)
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False