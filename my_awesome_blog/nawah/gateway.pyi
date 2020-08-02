from nawah.config import Config as Config
from typing import Any, List, Literal

def email_gateway(subject: str, addr_to: str, content: str, content_format: Literal[html, plain]=..., files: List[None]=..., email_auth: None=...) -> Any: ...

class Gateway:
    @staticmethod
    def send(gateway: str, **kwargs: Any) -> Any: ...
