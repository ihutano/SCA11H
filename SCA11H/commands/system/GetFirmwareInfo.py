import json

from SCA11H.commands.base.GetCommand import GetCommand


class FirmwareVersions:
    def __init__(self, payload):
        self.file_system_version = payload['fs_ver']
        self.backup_file_system_version = payload['bfs_ver']
        self.main_firmware_version = payload['fw_ver']
        self.backup_main_firmware_version = payload['bfw_ver']
        self.device_configuration_table_version = payload['dct_ver']
        self.backup_device_configuration_table_version = payload['bdct_ver']
        self.wlan_firmware_version = payload['wlan_ver']
        self.bootloader_firmware_version = payload['boot_ver']
        self.ota_recovery_firmware_version = payload['ota_ver']

    def __str__(self):
        return json.dumps(self.__dict__)


class GetFirmwareInfo(GetCommand):
    """ Query All Firmware Info """

    def __init__(self, **kwargs):
        super().__init__(endpoint='/sys/fwinfo', **kwargs)

    def run(self, **kwargs) -> FirmwareVersions:
        return FirmwareVersions(payload=super().run())

    @staticmethod
    def get_parser_name():
        return 'get-firmware-info'

    @staticmethod
    def get_help():
        return 'Query All Firmware Info'
