import uuid

import pytest

from badlight.app import db
from badlight.user.apis import UserAPI
from badlight.user.models import User
from badlight.user.services import UserService

from ..factories.user import UserFactory


def test_get_user_by_uuid():
    user = UserService.create_user(
        first_name="test",
        last_name="test",
        email="test.test@email.com",
        password="password"
    )

    user_uuid = str(user.uuid)

    user_from_service = UserAPI.get_user_by_uuid(uuid=user_uuid)
    assert user_from_service is user

    non_existent_user = UserAPI.get_user_by_uuid(uuid=str(uuid.uuid4()))
    assert non_existent_user is None

    assert User.query.count() == 1


def test_get_user_by_email():
    user = UserFactory.build()

    db.session.add(user)
    db.session.commit()

    user_from_service = UserAPI.get_user_by_email(email=user.email)
    assert user_from_service is user

    non_existent_user = UserAPI.get_user_by_email(
        email=UserFactory._generate_random_email('doesnot', 'exist')
    )
    assert non_existent_user is None

    assert User.query.count() == 1


def test_create_user():
    user = UserService.create_user(
        first_name="fname",
        last_name="lname",
        email="fname.lname@email.com",
        password="password"
    )

    user_uuid = str(user.uuid)

    user_from_service = UserAPI.get_user_by_uuid(uuid=user_uuid)
    assert user_from_service == user
    assert User.query.count() == 1
