class HttpResponse:
    def __init__(self, content=b"", *args, **kwargs):
        self.content = content

__all__ = [
    "HttpResponse"
]
