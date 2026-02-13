"""
"""

__version__ = "1.1.0.dev0"

from . import http
from .http.request import (
    HttpRequest
)

from .http.response import (
    HttpResponse
)

__all__ = list(
    {"http", "exceptions"} |
    set(http.request.__all__) |
    set(http.response.__all__) |
    {"__version__"}
)

def __getattr__(attr):
    pass

def __dir__():
    pass
