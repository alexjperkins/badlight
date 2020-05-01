from ..models import User
from ..services import UserService


class UserAPI:
    @staticmethod
    def get_user_by_uuid(*, uuid: str) -> User:
        return UserService.get_user_by_uuid(uuid=uuid)

    @staticmethod
    def get_user_by_email(*, email: str) -> User:
        return UserService.get_user_by_email(email=email)
