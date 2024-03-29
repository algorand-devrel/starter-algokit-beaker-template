from pathlib import Path

from beaker import *
from pyteal import *

from utils import build

app = Application("HelloWorld")


@app.external
def hello(name: abi.String, *, output: abi.String) -> Expr:
    return output.set(Concat(Bytes("Hello, "), name.get()))


@app.delete(bare=True, authorize=Authorize.only(Global.creator_address()))
def delete() -> Expr:
    return Approve()


if __name__ == "__main__":
    root_path = Path(__file__).parent
    build(root_path / "artifacts", app)
