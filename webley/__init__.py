"""
"""

from .app import Webley

__all__ = list(
    {"Webley"}
)

def __getattr__(attr):
    import warnings

    if attr == "exceptions":
        import webley.exceptions as exceptions
        return exceptions
    
    raise AttributeError(f"module {__name__!r} has no attribute {attr!r}")

def __dir__():
    pass
