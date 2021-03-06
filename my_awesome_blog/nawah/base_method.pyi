from aiohttp.web import WebSocketResponse as WebSocketResponse
from nawah.classes import ATTR_MOD as ATTR_MOD, BaseModel as BaseModel, DictObj as DictObj, JSONEncoder as JSONEncoder, NAWAH_DOC as NAWAH_DOC, NAWAH_QUERY as NAWAH_QUERY, PERM as PERM, Query as Query
from nawah.config import Config as Config
from nawah.enums import Event as Event, NAWAH_VALUES as NAWAH_VALUES
from nawah.utils import ConvertAttrException as ConvertAttrException, InvalidAttrException as InvalidAttrException, validate_attr as validate_attr
from typing import Any, AsyncGenerator, Dict, List, Set, Tuple, Union

logger: Any

class BaseMethod:
    module: Any = ...
    method: Any = ...
    permissions: Any = ...
    query_args: Any = ...
    doc_args: Any = ...
    watch_method: Any = ...
    get_method: Any = ...
    post_method: Any = ...
    def __init__(self, module: BaseModule, method: str, permissions: List[PERM], query_args: List[Dict[str, Union[str, Tuple[Any], Set[str]]]], doc_args: List[Dict[str, Union[str, Tuple[Any], Set[str]]]], watch_method: bool, get_method: bool, post_method: bool) -> None: ...
    async def validate_args(self, args: Dict[str, Any], args_list: str) -> Any: ...
    async def __call__(self, *, skip_events: List[Event]=..., env: Dict[str, Any]=..., query: Union[NAWAH_QUERY, Query]=..., doc: NAWAH_DOC=..., call_id: str=...) -> DictObj: ...
    async def return_results(self, ws: WebSocketResponse, results: DictObj, call_id: str) -> Union[None, DictObj]: ...
    async def watch_loop(self, ws: WebSocketResponse, stream: AsyncGenerator, call_id: str, watch_task: Dict[str, Any]) -> Any: ...
