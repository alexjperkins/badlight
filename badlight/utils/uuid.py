from uuid import UUID


def is_uuid_valid(*, uuid: str, version=4) -> bool:
    try:
        UUID(uuid, version=version)
    except ValueError:
        return False

    return True
