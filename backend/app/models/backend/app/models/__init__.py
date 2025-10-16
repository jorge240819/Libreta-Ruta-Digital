# Deja este archivo para que Python trate 'models' como paquete
# y luego Alembic pueda importar los modelos.
from app.models.user import User  # noqa: F401
