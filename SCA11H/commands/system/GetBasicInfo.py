from SCA11H.commands.base.GetCommand import GetCommand
from typing import Dict
import json


class SystemInfo:
    def __init__(self, payload: Dict[str, str]):
        self.uuid = payload['uuid']
        self.name = payload['name']
        self.alias = payload['alias']
        self.main_firmware_version = payload['fw_ver']
        self.wlan_firmware_version = payload['wlan_ver']
        self.file_system_version = payload['fs_ver']

    def __str__(self):
        return json.dumps(self.__dict__)


class GetBasicInfo(GetCommand):
    """ Query Basic System Info """

    def __init__(self, **kwargs):
        super().__init__(endpoint='/sys', **kwargs)

    def run(self, **kwargs) -> SystemInfo:
        return SystemInfo(payload=super().run())

    @staticmethod
    def get_parser_name():
        return 'get-basic-info'

    @staticmethod
    def get_help():
        return 'Query Basic System Info'
