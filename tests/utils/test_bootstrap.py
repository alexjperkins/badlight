import pytest

from badlight.app import _PROJECT_ROOT
from badlight.user.models import User
from badlight.utils.bootstrap import bootstrap_models


@pytest.fixture
def expected_registered_models():
    return (
        User,
    )


def test_gather_models(expected_registered_models):
    models = [model for model in bootstrap_models(project_root=_PROJECT_ROOT)]
    assert len(models) == len(expected_registered_models)
    assert set(models) == set(expected_registered_models)
