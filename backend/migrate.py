from alembic.config import Config
from alembic import command

alembic_cfg = Config("alembic.ini")  # faylingiz ildiz papkada bo‘lishi kerak
command.upgrade(alembic_cfg, "head")
