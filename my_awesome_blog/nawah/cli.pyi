import argparse
from typing import Any, Literal

logger: Any
handler: Any
formatter: Any

def nawah_cli() -> None: ...
def install_deps(args: argparse.Namespace) -> Any: ...
def launch(args: argparse.Namespace, custom_launch: Literal[test, generate_ref, generate_models]=...) -> Any: ...
def test(args: argparse.Namespace) -> Any: ...
def generate_ref(args: argparse.Namespace) -> Any: ...
