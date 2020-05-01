import uuid

import pytest

from badlight.utils.uuid import is_uuid_valid


@pytest.mark.parametrize(
    'uuid_to_test, expected_validity',
    [
        (str(uuid.uuid4()), True),
        ("not_valid", False),
    ],
)
def test_validate_uuid(uuid_to_test, expected_validity):
    assert is_uuid_valid(uuid=uuid_to_test, version=4) == expected_validity
