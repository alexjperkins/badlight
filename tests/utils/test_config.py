from contextlib import suppress as do_not_raise

import pytest
from werkzeug.utils import ImportStringError

from badlight.utils.config import initialize_config


@pytest.mark.parametrize(
    ('environment, expected_raises'),
    [
        ('local', do_not_raise()),
        ('production', do_not_raise()),
        ('testing', do_not_raise()),
        ('does_not_exist', pytest.raises(ModuleNotFoundError)),
    ],
)
def test_initialize_config(app, environment, expected_raises):
    with expected_raises:
        val = initialize_config(app=app, environment=environment)
        assert val is app
