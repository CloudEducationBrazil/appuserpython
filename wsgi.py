from app import create_app, db

app = create_app()

# Cria tabelas automaticamente no deploy
with app.app_context():
    db.create_all()