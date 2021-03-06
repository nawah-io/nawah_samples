import datetime
import json
from bson import binary as binary
from dataclasses import field as field
from nawah.enums import Event as Event, NAWAH_VALUES as NAWAH_VALUES
from typing import Any, Callable, Dict, List, Literal, Tuple, Type, Union

logger: Any
NAWAH_EVENTS = List[Event]
NAWAH_ENV: Any
NAWAH_QUERY: Any
NAWAH_DOC: Any
ATTRS_TYPES: Dict[str, Dict[str, Type]]

class L10N(dict): ...

class NAWAH_MODULE:
    collection: Union[str, bool]
    proxy: str
    attrs: Dict[str, ATTR]
    diff: Union[bool, ATTR_MOD]
    defaults: Dict[str, Any]
    unique_attrs: List[str]
    extns: Dict[str, EXTN]
    privileges: List[str]
    methods: None
    cache: List[CACHE]
    analytics: List[ANALYTIC]
    package_name: str
    module_name: str
    async def pre_read(self, skip_events: NAWAH_EVENTS, env: NAWAH_ENV, query: Union[NAWAH_QUERY, Query], doc: NAWAH_DOC, payload: Dict[str, Any]) -> Tuple[NAWAH_EVENTS, NAWAH_ENV, Union[NAWAH_QUERY, Query], NAWAH_DOC, Dict[str, Any]]: ...
    async def on_read(self, results: Dict[str, Any], skip_events: NAWAH_EVENTS, env: NAWAH_ENV, query: Union[NAWAH_QUERY, Query], doc: NAWAH_DOC, payload: Dict[str, Any]) -> Tuple[Dict[str, Any], NAWAH_EVENTS, NAWAH_ENV, Union[NAWAH_QUERY, Query], NAWAH_DOC, Dict[str, Any]]: ...
    async def read(self, skip_events: NAWAH_EVENTS=..., env: NAWAH_ENV=..., query: Union[NAWAH_QUERY, Query]=..., doc: NAWAH_DOC=...) -> DictObj: ...
    async def pre_create(self, skip_events: NAWAH_EVENTS, env: NAWAH_ENV, query: Union[NAWAH_QUERY, Query], doc: NAWAH_DOC, payload: Dict[str, Any]) -> Tuple[NAWAH_EVENTS, NAWAH_ENV, Union[NAWAH_QUERY, Query], NAWAH_DOC, Dict[str, Any]]: ...
    async def on_create(self, results: Dict[str, Any], skip_events: NAWAH_EVENTS, env: NAWAH_ENV, query: Union[NAWAH_QUERY, Query], doc: NAWAH_DOC, payload: Dict[str, Any]) -> Tuple[Dict[str, Any], NAWAH_EVENTS, NAWAH_ENV, Union[NAWAH_QUERY, Query], NAWAH_DOC, Dict[str, Any]]: ...
    async def create(self, skip_events: NAWAH_EVENTS=..., env: NAWAH_ENV=..., query: Union[NAWAH_QUERY, Query]=..., doc: NAWAH_DOC=...) -> DictObj: ...
    async def pre_update(self, skip_events: NAWAH_EVENTS, env: NAWAH_ENV, query: Union[NAWAH_QUERY, Query], doc: NAWAH_DOC, payload: Dict[str, Any]) -> Tuple[NAWAH_EVENTS, NAWAH_ENV, Union[NAWAH_QUERY, Query], NAWAH_DOC, Dict[str, Any]]: ...
    async def on_update(self, results: Dict[str, Any], skip_events: NAWAH_EVENTS, env: NAWAH_ENV, query: Union[NAWAH_QUERY, Query], doc: NAWAH_DOC, payload: Dict[str, Any]) -> Tuple[Dict[str, Any], NAWAH_EVENTS, NAWAH_ENV, Union[NAWAH_QUERY, Query], NAWAH_DOC, Dict[str, Any]]: ...
    async def update(self, skip_events: NAWAH_EVENTS=..., env: NAWAH_ENV=..., query: Union[NAWAH_QUERY, Query]=..., doc: NAWAH_DOC=...) -> DictObj: ...
    async def pre_delete(self, skip_events: NAWAH_EVENTS, env: NAWAH_ENV, query: Union[NAWAH_QUERY, Query], doc: NAWAH_DOC, payload: Dict[str, Any]) -> Tuple[NAWAH_EVENTS, NAWAH_ENV, Union[NAWAH_QUERY, Query], NAWAH_DOC, Dict[str, Any]]: ...
    async def on_delete(self, results: Dict[str, Any], skip_events: NAWAH_EVENTS, env: NAWAH_ENV, query: Union[NAWAH_QUERY, Query], doc: NAWAH_DOC, payload: Dict[str, Any]) -> Tuple[Dict[str, Any], NAWAH_EVENTS, NAWAH_ENV, Union[NAWAH_QUERY, Query], NAWAH_DOC, Dict[str, Any]]: ...
    async def delete(self, skip_events: NAWAH_EVENTS=..., env: NAWAH_ENV=..., query: Union[NAWAH_QUERY, Query]=..., doc: NAWAH_DOC=...) -> DictObj: ...
    async def pre_create_file(self, skip_events: NAWAH_EVENTS, env: NAWAH_ENV, query: Union[NAWAH_QUERY, Query], doc: NAWAH_DOC, payload: Dict[str, Any]) -> Tuple[NAWAH_EVENTS, NAWAH_ENV, Union[NAWAH_QUERY, Query], NAWAH_DOC, Dict[str, Any]]: ...
    async def on_create_file(self, results: Dict[str, Any], skip_events: NAWAH_EVENTS, env: NAWAH_ENV, query: Union[NAWAH_QUERY, Query], doc: NAWAH_DOC, payload: Dict[str, Any]) -> Tuple[Dict[str, Any], NAWAH_EVENTS, NAWAH_ENV, Union[NAWAH_QUERY, Query], NAWAH_DOC, Dict[str, Any]]: ...
    async def create_file(self, skip_events: NAWAH_EVENTS=..., env: NAWAH_ENV=..., query: Union[NAWAH_QUERY, Query]=..., doc: NAWAH_DOC=...) -> DictObj: ...
    async def pre_delete_file(self, skip_events: NAWAH_EVENTS, env: NAWAH_ENV, query: Union[NAWAH_QUERY, Query], doc: NAWAH_DOC, payload: Dict[str, Any]) -> Tuple[NAWAH_EVENTS, NAWAH_ENV, Union[NAWAH_QUERY, Query], NAWAH_DOC, Dict[str, Any]]: ...
    async def on_delete_file(self, results: Dict[str, Any], skip_events: NAWAH_EVENTS, env: NAWAH_ENV, query: Union[NAWAH_QUERY, Query], doc: NAWAH_DOC, payload: Dict[str, Any]) -> Tuple[Dict[str, Any], NAWAH_EVENTS, NAWAH_ENV, Union[NAWAH_QUERY, Query], NAWAH_DOC, Dict[str, Any]]: ...
    async def delete_file(self, skip_events: NAWAH_EVENTS=..., env: NAWAH_ENV=..., query: Union[NAWAH_QUERY, Query]=..., doc: NAWAH_DOC=...) -> DictObj: ...

class InvalidAttrTypeException(Exception):
    attr_type: Any = ...
    def __init__(self, attr_type: str) -> None: ...

class InvalidAttrTypeArgException(Exception):
    arg_name: Any = ...
    arg_type: Any = ...
    arg_val: Any = ...
    def __init__(self, arg_name: str, arg_type: Any, arg_val: Any) -> None: ...

class InvalidAttrTypeArgsException(Exception):
    msg: Any = ...
    def __init__(self, msg: str) -> None: ...

class ATTR:
    def __init__(self, attr_type: str, *, desc: str=..., **kwargs: Dict[str, Any]) -> None: ...
    @classmethod
    def ANY(cls: Any, *, desc: str=...) -> Any: ...
    @classmethod
    def ACCESS(cls: Any, *, desc: str=...) -> Any: ...
    @classmethod
    def COUNTER(cls: Any, *, desc: str=..., pattern: str, values: List[Callable]=...) -> Any: ...
    @classmethod
    def ID(cls: Any, *, desc: str=...) -> Any: ...
    @classmethod
    def STR(cls: Any, *, desc: str=..., pattern: str=...) -> Any: ...
    @classmethod
    def INT(cls: Any, *, desc: str=..., ranges: List[List[int]]=...) -> Any: ...
    @classmethod
    def FLOAT(cls: Any, *, desc: str=..., ranges: List[List[int]]=...) -> Any: ...
    @classmethod
    def BOOL(cls: Any, *, desc: str=...) -> Any: ...
    @classmethod
    def LOCALE(cls: Any, *, desc: str=...) -> Any: ...
    @classmethod
    def LOCALES(cls: Any, *, desc: str=...) -> Any: ...
    @classmethod
    def EMAIL(cls: Any, *, desc: str=..., allowed_domains: List[str]=..., disallowed_domains: List[str]=..., strict: bool=...) -> Any: ...
    @classmethod
    def PHONE(cls: Any, *, desc: str=..., codes: List[str]=...) -> Any: ...
    @classmethod
    def IP(cls: Any, *, desc: str=...) -> Any: ...
    @classmethod
    def URI_WEB(cls: Any, *, desc: str=..., allowed_domains: List[str]=..., disallowed_domains: List[str]=..., strict: bool=...) -> Any: ...
    @classmethod
    def DATETIME(cls: Any, *, desc: str=..., ranges: List[List[str]]=...) -> Any: ...
    @classmethod
    def DATE(cls: Any, *, desc: str=..., ranges: List[List[str]]=...) -> Any: ...
    @classmethod
    def DYNAMIC_ATTR(cls: Any, *, desc: str=..., types: List[str]=...) -> Any: ...
    @classmethod
    def DYNAMIC_VAL(cls: Any, *, desc: str=..., dynamic_attr: str) -> Any: ...
    @classmethod
    def TIME(cls: Any, *, desc: str=..., ranges: List[List[str]]=...) -> Any: ...
    @classmethod
    def FILE(cls: Any, *, desc: str=..., types: List[str]=..., max_ratio: List[int]=..., min_ratio: List[int]=..., max_dims: List[int]=..., min_dims: List[int]=..., max_size: int=...) -> Any: ...
    @classmethod
    def GEO(cls: Any, *, desc: str=...) -> Any: ...
    @classmethod
    def LIST(cls: Any, *, desc: str=..., list: List[ATTR], min: int=..., max: int=...) -> Any: ...
    @classmethod
    def KV_DICT(cls: Any, *, desc: str=..., key: ATTR, val: ATTR, min: int=..., max: int=..., req: List[str]=...) -> Any: ...
    @classmethod
    def TYPED_DICT(cls: Any, *, desc: str=..., dict: Dict[str, ATTR]) -> Any: ...
    @classmethod
    def LITERAL(cls: Any, *, desc: str=..., literal: List[Union[str, int, float, bool]]) -> Any: ...
    @classmethod
    def UNION(cls: Any, *, desc: str=..., union: List[ATTR]) -> Any: ...
    @classmethod
    def TYPE(cls: Any, *, desc: str=..., type: str) -> Any: ...
    @classmethod
    def validate_type(cls: Any, attr_type: ATTR, *, skip_type: bool=...) -> Any: ...
    @classmethod
    def validate_arg(cls: Any, arg_name: str, arg_type: Any, arg_val: Any) -> Any: ...

class ATTR_MOD:
    condition: Callable
    default: Union[Callable, Any]
    def __init__(self, condition: Callable[[List[str], Dict[str, Any], Query, NAWAH_DOC], bool], default: Union[Callable[[List[str], Dict[str, Any], Query, NAWAH_DOC], Any], Any]) -> None: ...

class PERM:
    privilege: str
    query_mod: Union[NAWAH_DOC, List[NAWAH_DOC]]
    doc_mod: Union[NAWAH_DOC, List[NAWAH_DOC]]
    def __init__(self, privilege: str, *, query_mod: Union[NAWAH_DOC, List[NAWAH_DOC]]=..., doc_mod: Union[NAWAH_DOC, List[NAWAH_DOC]]=...) -> None: ...

class EXTN:
    module: str
    query: NAWAH_QUERY
    attrs: List[str]
    force: bool = ...
    def __init__(self, module: str, *, query: NAWAH_QUERY=..., attrs: List[str], force: bool=...) -> None: ...

class CACHE:
    condition: Callable[[List[str], Dict[str, Any], Union[Query, NAWAH_QUERY]], bool]
    period: int
    queries: Dict[str, CACHED_QUERY]
    def __init__(self, condition: Callable[[List[str], Dict[str, Any], Union[Query, NAWAH_QUERY]], bool], *, period: int=...) -> None: ...
    def cache_query(self, query_key: str, results: DictObj) -> Any: ...

class CACHED_QUERY:
    results: DictObj
    query_time: datetime.datetime
    def __init__(self, results: DictObj, *, query_time: datetime.datetime=...) -> None: ...

class ANALYTIC:
    condition: Callable[[List[str], Dict[str, Any], Union[Query, NAWAH_QUERY], NAWAH_DOC], bool]
    doc: Callable[[List[str], Dict[str, Any], Union[Query, NAWAH_QUERY], NAWAH_DOC], NAWAH_DOC]
    def __init__(self, condition: Callable[[List[str], Dict[str, Any], Union[Query, NAWAH_QUERY], NAWAH_DOC], bool], doc: Callable[[List[str], Dict[str, Any], Union[Query, NAWAH_QUERY], NAWAH_DOC], NAWAH_DOC]) -> None: ...

class PACKAGE_CONFIG:
    api_level: str = ...
    version: str = ...
    emulate_test: bool = ...
    debug: bool = ...
    port: int = ...
    env: str = ...
    force_admin_check: bool = ...
    vars: Dict[str, Any] = ...
    client_apps: Dict[str, None] = ...
    analytics_events: None = ...
    conn_timeout: int = ...
    quota_anon_min: int = ...
    quota_auth_min: int = ...
    quota_ip_min: int = ...
    data_server: str = ...
    data_name: str = ...
    data_ssl: bool = ...
    data_ca_name: str = ...
    data_ca: str = ...
    data_disk_use: bool = ...
    data_azure_mongo: bool = ...
    email_auth: Dict[str, str] = ...
    locales: List[str] = ...
    locale: str = ...
    admin_doc: NAWAH_DOC = ...
    admin_password: str = ...
    anon_token: str = ...
    anon_privileges: Dict[str, List[str]] = ...
    user_attrs: Dict[str, ATTRS_TYPES] = ...
    user_settings: Dict[str, Dict[Literal[type, val], Union[Literal[user, user_sys], Any]]] = ...
    user_doc_settings: List[str] = ...
    groups: List[Dict[str, Any]] = ...
    default_privileges: Dict[str, List[str]] = ...
    data_indexes: List[Dict[str, Any]] = ...
    docs: List[Dict[str, Any]] = ...
    jobs: List[Dict[str, Any]] = ...
    gateways: Dict[str, Callable] = ...
    types: Dict[str, Callable] = ...
    def __init__(self, api_level: Any, version: Any, emulate_test: Any, debug: Any, port: Any, env: Any, force_admin_check: Any, vars: Any, client_apps: Any, analytics_events: Any, conn_timeout: Any, quota_anon_min: Any, quota_auth_min: Any, quota_ip_min: Any, data_server: Any, data_name: Any, data_ssl: Any, data_ca_name: Any, data_ca: Any, data_disk_use: Any, data_azure_mongo: Any, email_auth: Any, locales: Any, locale: Any, admin_doc: Any, admin_password: Any, anon_token: Any, anon_privileges: Any, user_attrs: Any, user_settings: Any, user_doc_settings: Any, groups: Any, default_privileges: Any, data_indexes: Any, docs: Any, jobs: Any, gateways: Any, types: Any) -> None: ...

class APP_CONFIG(PACKAGE_CONFIG):
    name: str = ...
    version: str = ...
    debug: bool = ...
    port: int = ...
    env: str = ...
    envs: Dict[str, PACKAGE_CONFIG] = ...
    realm: bool = ...
    force_admin_check: bool = ...
    def __init__(self, api_level: Any, version: Any, emulate_test: Any, debug: Any, port: Any, env: Any, force_admin_check: Any, vars: Any, client_apps: Any, analytics_events: Any, conn_timeout: Any, quota_anon_min: Any, quota_auth_min: Any, quota_ip_min: Any, data_server: Any, data_name: Any, data_ssl: Any, data_ca_name: Any, data_ca: Any, data_disk_use: Any, data_azure_mongo: Any, email_auth: Any, locales: Any, locale: Any, admin_doc: Any, admin_password: Any, anon_token: Any, anon_privileges: Any, user_attrs: Any, user_settings: Any, user_doc_settings: Any, groups: Any, default_privileges: Any, data_indexes: Any, docs: Any, jobs: Any, gateways: Any, types: Any, name: Any, envs: Any, realm: Any) -> None: ...

class JSONEncoder(json.JSONEncoder):
    def default(self, o: Any): ...

class DictObj:
    def __init__(self, attrs: Any) -> None: ...
    def __deepcopy__(self, memo: Any): ...
    def __getattr__(self, attr: Any): ...
    def __setattr__(self, attr: Any, val: Any) -> None: ...
    def __getitem__(self, attr: Any): ...
    def __setitem__(self, attr: Any, val: Any) -> None: ...
    def __delitem__(self, attr: Any) -> None: ...
    def __contains__(self, attr: Any): ...

class BaseModel(DictObj):
    def __init__(self, attrs: Any) -> None: ...

class InvalidQueryArgException(Exception):
    arg_name: Any = ...
    arg_oper: Any = ...
    arg_type: Any = ...
    arg_val: Any = ...
    def __init__(self, arg_name: str, arg_oper: Literal['$ne', '$eq', '$gt', '$gte', '$lt', '$lte', '$bet', '$all', '$in', '$nin', '$regex'], arg_type: Any, arg_val: Any) -> None: ...

class UnknownQueryArgException(Exception):
    arg_name: Any = ...
    arg_oper: Any = ...
    def __init__(self, arg_name: str, arg_oper: Literal['$ne', '$eq', '$gt', '$gte', '$lt', '$lte', '$bet', '$all', '$in', '$nin', '$regex']) -> None: ...

class Query(list):
    def __init__(self, query: Union[NAWAH_QUERY, Query]) -> None: ...
    def __deepcopy__(self, memo: Any): ...
    def append(self, obj: Any) -> Any: ...
    def __contains__(self, attr: str) -> Any: ...
    def __getitem__(self, attr: str) -> Any: ...
    def __setitem__(self, attr: str, val: Any) -> Any: ...
    def __delitem__(self, attr: str) -> Any: ...
    @classmethod
    def validate_arg(cls, arg_name: Any, arg_oper: Any, arg_val: Any) -> None: ...

class QueryAttrList(list):
    def __init__(self, query: Query, attrs: List[str], paths: List[List[int]], indexes: List[int], vals: List[Any]) -> None: ...
    def __setitem__(self, item: Union[Literal['*'], int], val: Any) -> Any: ...
    def __delitem__(self, item: Union[Literal['*'], int]) -> Any: ...
    def replace_attr(self, item: Union[Literal['*'], int], new_attr: str) -> Any: ...
