import typing as t
from urllib.parse import parse_qs

from webley.http import Response

if t.TYPE_CHECKING:
    from _typeshed.wsgi import StartResponse, WSGIEnvironment

class Webley:
    def __init__(self, project_name: str) -> None:
        self.project_name = project_name

    def __repr__(self) -> str:
        return f""

    def run(
        self,
        host: str = "127.0.0.1",
        port: int = 5000
    ) -> None:
        from wsgiref.simple_server import make_server

        try:
            with make_server(host, port, self) as httpd:
                httpd.serve_forever()
        finally:
            pass

    def wsgi_app(
        self, environ, start_response
    ) -> t.Any:
        pass

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)
