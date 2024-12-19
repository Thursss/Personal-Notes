import pkgutil
import importlib


def import_submodules(package):
    submodules = []

    for name in pkgutil.walk_packages(package.__path__):
        modules = importlib.import_module(name)
        submodules.append(modules)

    return submodules
