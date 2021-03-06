from motor.motor_asyncio import AsyncIOMotorClient as AsyncIOMotorClient
from nawah.classes import APP_CONFIG as APP_CONFIG, ATTR as ATTR, BaseModel as BaseModel, DictObj as DictObj, NAWAH_DOC as NAWAH_DOC, NAWAH_MODULE as NAWAH_MODULE, PACKAGE_CONFIG as PACKAGE_CONFIG
from nawah.enums import Event as Event, LOCALE_STRATEGY as LOCALE_STRATEGY
from nawah.utils import deep_update as deep_update, generate_attr as generate_attr
from typing import Any, Callable, Dict, List, Literal, Union

logger: Any

def process_config(config: Union[APP_CONFIG, PACKAGE_CONFIG], *, pkgname: str=...) -> Any: ...

class Config:
    debug: bool = ...
    env: str = ...
    port: int = ...
    packages_api_levels: Dict[str, str] = ...
    packages_versions: Dict[str, str] = ...
    test: str = ...
    test_skip_flush: bool = ...
    test_force: bool = ...
    test_env: bool = ...
    test_breakpoint: bool = ...
    test_collections: bool = ...
    tests: Dict[str, List[STEP]] = ...
    emulate_test: bool = ...
    force_admin_check: bool = ...
    generate_ref: bool = ...
    realm: bool = ...
    vars: Dict[str, Any] = ...
    client_apps: Dict[str, None] = ...
    analytics_events: None = ...
    conn_timeout: int = ...
    quota_anon_min: int = ...
    quota_auth_min: int = ...
    quota_ip_min: int = ...
    file_upload_limit: int = ...
    file_upload_timeout: int = ...
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
    locale_strategy: LOCALE_STRATEGY = ...
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
    l10n: Dict[str, Dict[str, Any]] = ...
    jobs: List[Dict[str, Any]] = ...
    gateways: Dict[str, Callable] = ...
    types: Dict[str, Callable] = ...
    modules: Dict[str, NAWAH_MODULE] = ...
    @classmethod
    async def config_data(cls: Any) -> None: ...
    @classmethod
    def compile_anon_user(cls): ...
    @classmethod
    def compile_anon_session(cls): ...
