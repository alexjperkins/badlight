import logging

from werkzeug.utils import import_string, ImportStringError


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    handlers=[logging.StreamHandler()],
)


def initialize_config(*, app, environment="local"):
    config_module_name = f"{environment.lower()}"
    config_class_name = f"{environment.capitalize()}Config"

    try:
        cfg = import_string(f"config.{config_module_name}.{config_class_name}")

    except ImportStringError:
        logger.error("Error: Cannot import module %s", config_module_name)
        raise ModuleNotFoundError

    app.config.from_object(cfg())
    return app
