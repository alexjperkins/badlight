import pytest

from badlight.app import db
from badlight.user.models import User
from ..factories.user import UserFactory


@pytest.fixture(autouse=True)
def shared_db_session(_shared_db_session):
    yield
    User.query.delete()


@pytest.fixture(scope="module")
def commit_user():
    user = UserFactory.build()
    db.session.add(user)
    db.session.commit()
    yield


@pytest.fixture(scope="module")
def commit_many_user():
    for user in UserFactory.build_many(how_many=3):
        db.session.add(user)

    db.session.commit()
    yield
