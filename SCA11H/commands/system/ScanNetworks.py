from SCA11H.commands.base.GetCommand import GetCommand
from SCA11H.commands.system.NetworkSecurityType import NetworkSecurityType
from SCA11H.commands.base import enum_from_value
from typing import List
import json


class NetworkInfo:
    def __init__(self, payload):
        self.ssid = payload[0]
        self.bssid = payload[1]
        self.security = enum_from_value(NetworkSecurityType, payload[2])
        self.channel = payload[3]
        self.signal_strength = payload[4]

    def __str__(self):
        return json.dumps({
            'ssid': self.ssid,
            'bssid': self.bssid,
            'security': self.security.value,
            'channel': self.channel,
            'signal_strength': self.signal_strength,
        })

    def __repr__(self):
        prefix = NetworkInfo.__name__
        return '%s(%s)' % (prefix, [self.ssid, self.bssid, self.security.value, self.channel, self.signal_strength])


class ScanNetworks(GetCommand):
    """ Scan networks results """

    def __init__(self, **kwargs):
        super().__init__(endpoint='/sys/scan', **kwargs)

    def run(self, **kwargs) -> List[NetworkInfo]:
        res = super().run()
        return [NetworkInfo(payload=x) for x in res['networks']]

    @staticmethod
    def get_parser_name():
        return 'scan-networks'

    @staticmethod
    def get_help():
        return 'Scan networks results'
