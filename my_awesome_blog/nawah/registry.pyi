from nawah.classes import NAWAH_MODULE as NAWAH_MODULE
from nawah.config import Config as Config
from typing import Any, Dict, List

logger: Any

class InvalidModuleException(Exception):
    module: Any = ...
    def __init__(self, module: Any) -> None: ...

class InvalidLocaleException(Exception):
    locale: Any = ...
    def __init__(self, locale: Any) -> None: ...

class InvalidLocaleTermException(Exception):
    locale: Any = ...
    term: Any = ...
    def __init__(self, locale: Any, term: Any) -> None: ...

class InvalidVarException(Exception):
    var: Any = ...
    def __init__(self, var: Any) -> None: ...

class Registry:
    docs: List[Dict[str, Any]] = ...
    jobs: List[Dict[str, Any]] = ...
    @staticmethod
    def module(module: str) -> NAWAH_MODULE: ...
    @staticmethod
    def l10n(locale: str, term: str) -> Any: ...
    @staticmethod
    def var(var: str) -> Any: ...
