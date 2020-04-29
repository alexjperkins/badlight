import os


def _build_database_connection_uri_string(
    *, user, password, host, port, db,
):
    return f"postgres://{user}:{password}@{host}:{port}/{db}"


def _gather_db_env_variables():
    db_env = ("USER", "PASSWORD", "HOST", "PORT", "DB")
    for to_gather in db_env:
        try:
            env_var = os.environ[f"POSTGRES_{to_gather}"]
        except KeyError:
            raise KeyError(
                f"Missing ``POSTGRES_{to_gather}`` "
                f"db connection param from environment..."
            )
        else:
            yield env_var


def build_database_connection_uri_string(*, environment):
    if environment.lower() in ("local", "testing"):
        user, password, host, port, db = _gather_db_env_variables()
        if environment.lower() == "testing":
            db += "_testing"

        return _build_database_connection_uri_string(
            user=user, password=password, host=host, port=port, db=db
        )

    raise RuntimeError("Incorrectly setup environment: %s", environment.lower())
