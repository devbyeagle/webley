import typing as t

from webley.http import Response

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
        pass
