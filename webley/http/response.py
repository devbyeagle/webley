class HttpResponse:
    def __init__(self, content=b"", *args, **kwargs) -> None:
        self.content = content
