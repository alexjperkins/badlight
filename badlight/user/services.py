from .models import User
from ..app import db
from ..utils.uuid import is_uuid_valid


class UserService:
    @staticmethod
    def get_user_by_uuid(*, uuid: str) -> User:
        if not is_uuid_valid(uuid=uuid):
            return None

        return User.query.filter_by(uuid=uuid).one_or_none()

    @staticmethod
    def get_user_by_email(*, email: str) -> User:
        return User.query.filter_by(email=email).one_or_none()

    @staticmethod
    def create_user(
        *, first_name: str, last_name: str, email: str, password: str,
    ) -> User:
        user = User(
            first_name=first_name, last_name=last_name, email=email, password=password
        )

        db.session.add(user)
        db.session.commit()
        return user
