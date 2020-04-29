import random
import string
from typing import List, Tuple

from badlight.user.models import User


class UserFactory:
    @classmethod
    def build(cls, *, password=None) -> User:

        first_name = cls._generate_random_name()
        last_name = cls._generate_random_name()
        email = cls._generate_random_email(first_name, last_name)
        password = password or cls._generate_random_password()

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        return user

    @classmethod
    def build_many(cls, *, how_many) -> List[User]:
        return [cls.build() for _ in range(how_many)]

    @classmethod
    def build_and_return_password(cls) -> Tuple[User, str]:
        password = cls._generate_random_password()
        return cls.build(password=password), password

    @staticmethod
    def _generate_random_name(length=8):
        return "".join(random.choice(string.ascii_lowercase) for _ in range(length))

    @staticmethod
    def _generate_random_email(fn , ln):
        return (
            f"{fn}.{ln}"
            f"@email.com"
        )

    @staticmethod
    def _generate_random_password(length=32):
        return "".join(random.choice(string.hexdigits) for _ in range(length))
