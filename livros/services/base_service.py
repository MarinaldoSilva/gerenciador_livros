from typing import Any
from users.models import User

class BaseLivroService:
    def __init__(self, user:User):
        self.user = user