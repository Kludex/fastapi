from typing import Any, Sequence, Type

from pydantic import BaseModel, ValidationError, create_model
from pydantic.error_wrappers import ErrorList
from starlette.exceptions import HTTPException as HTTPException  # noqa: F401
from starlette.exceptions import WebSocketException as WebSocketException  # noqa: F401

RequestErrorModel: Type[BaseModel] = create_model("Request")
WebSocketErrorModel: Type[BaseModel] = create_model("WebSocket")


class FastAPIError(RuntimeError):
    """
    A generic, FastAPI-specific error.
    """


class RequestValidationError(ValidationError):
    def __init__(self, errors: Sequence[ErrorList], *, body: Any = None) -> None:
        self.body = body
        super().__init__(errors, RequestErrorModel)


class WebSocketRequestValidationError(ValidationError):
    def __init__(self, errors: Sequence[ErrorList]) -> None:
        super().__init__(errors, WebSocketErrorModel)
