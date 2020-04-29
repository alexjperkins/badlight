from badlight.app import db

from ..factories.user import UserFactory


def test_user_model():
    user, password = UserFactory.build_and_return_password()

    assert user.first_name
    assert user.last_name

    assert user.name == f'{user.first_name} {user.last_name}'

    assert not any((
        user.is_authenticated,
        user.is_active,
        user.is_admin
    ))

    assert user.username == user.email

    assert user.password != password
    assert user.verify_password(password=password)
