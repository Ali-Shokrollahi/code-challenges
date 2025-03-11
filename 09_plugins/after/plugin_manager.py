from decimal import Decimal
import importlib
from importlib.util import module_from_spec, spec_from_file_location
from typing import Protocol
import os


class Plugin(Protocol):
    @staticmethod
    def get_payment_method() -> str:
        ...

    @staticmethod
    def process_payment(total: Decimal) -> None:
        ...


PLUGINS: dict[str, Plugin] = {}


def import_module(name: str, path: str) -> Plugin:
    """Imports a module from a file."""
    spec = spec_from_file_location(name, path)
    if spec:
        module: Plugin = module_from_spec(spec)  # type: ignore
        spec.loader.exec_module(module)  # type: ignore
        return module
    raise ImportError(f"Could not import {name} from {path}")


def load_plugins_from_folder(folder: str) -> None:
    """Loads all modules from a folder."""
    for root, _, files in os.walk(folder):
        for file in files:
            if not file.endswith(".py"):
                continue
            module_name = file[:-3]
            module_path = os.path.join(root, file)
            module = import_module(module_name, module_path)
            PLUGINS[module.get_payment_method()] = module


def get_plugin(name: str) -> Plugin:
    """Gets a plugin by name."""
    return PLUGINS[name]


def plugin_exists(name: str) -> bool:
    """Checks if a plugin exists."""
    return name in PLUGINS


def all_plugins() -> list[str]:
    """Gets all plugin names."""
    return list(PLUGINS.keys())
