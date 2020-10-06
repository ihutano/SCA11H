from SCA11H.commands.base.Command import Command, Method
from typing import Dict, Union, List


class GetCommand(Command):
    def __init__(self, endpoint: str, **kwargs):
        super().__init__(**kwargs)
        self.endpoint = endpoint

    def run(self, **kwargs) -> Dict[str, Union[str, int, Dict[str, str], List[Union[str, int]]]]:
        return super().run(method=Method.get, endpoint=self.endpoint, payload=None)

    def run_for_plaintext_result(self, **kwargs) -> str:
        return super().run_for_plaintext_result(method=Method.get, endpoint=self.endpoint, payload=None)
