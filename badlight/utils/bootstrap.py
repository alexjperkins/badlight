import os
from pathlib import Path
from typing import List

from flask_sqlalchemy.model import DefaultMeta
from werkzeug.utils import import_string


EXCLUDE_DIRS = [
    "__pycache__",
    "utils",
    "config",
    "migrations",
]


def _format_path_to_python_import(*, path):
    if path == "/":
        return ""

    return path.split("/")[-1]


def _gather_models(*, project_root):
    """Gathers all models throughout the directory."""
    for root, dirs, _ in os.walk(project_root):
        for _dir in dirs:
            if _dir in EXCLUDE_DIRS:
                continue

            for _, _, files in os.walk(Path(root) / Path(_dir)):
                if "models.py" in files:
                    module = import_string(
                        f"{_format_path_to_python_import(path=project_root)}.{_dir}."
                        f"models"
                    )
                    for model in module.__all__:
                        model = getattr(module, model)
                        if isinstance(model, DefaultMeta):
                            yield model


def bootstrap_models(*, project_root: Path) -> List:
    return list(_gather_models(project_root=str(project_root)))
