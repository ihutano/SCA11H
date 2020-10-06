from enum import Enum

from SCA11H.commands.base.GetCommand import GetCommand
from SCA11H.commands.system.NetworkSecurityType import NetworkSecurityType


class NetworkType(Enum):
    Station = 'sta'
    AccessPoint = 'ap'


class ActiveNetworkInfo:
    def __init__(self, network_type: NetworkType, payload):
        print(payload)
        self.network_type = network_type
        self.ssid = payload['ssid']
        self.security = NetworkSecurityType.from_string(payload['security'])
        self.password = payload.get('passphrase', None)
        self.channel = payload.get('channel', 11)
        self.dhcp_client_enabled = payload.get('dhcp', None)
        self.dhcp_server_enabled = payload.get('dhcpd', None)
        self.ip = payload.get('ip', None)
        self.netmask = payload.get('netmask', None)
        self.gateway = payload.get('gateway', None)
        self.dns_1 = payload.get('ipdns1', None)
        self.dns_2 = payload.get('ipdns2', None)

    def __str__(self):
        result = {
            'ssid': self.ssid,
            'security': self.security.value,
            'channel': self.channel,
            'type': self.network_type.value,
        }

        def add_field(name, value):
            if value is not None:
                nonlocal result
                result[name] = value

        add_field('password', self.password)
        add_field('dhcp_client_enabled', self.dhcp_client_enabled)
        add_field('dhcp_server_enabled', self.dhcp_server_enabled)
        add_field('ip', self.ip)
        add_field('netmask', self.netmask)
        add_field('gateway', self.gateway)
        add_field('dns_1', self.dns_1)
        add_field('dns_2', self.dns_2)

        return '%s' % result

    def __repr__(self):
        return '%s' % self.__str__()


class GetActiveNetworkInfo(GetCommand):
    """ Query Current Network Info """

    def __init__(self, **kwargs):
        super().__init__(endpoint='/sys/netinfo', **kwargs)

    def run(self, **kwargs) -> ActiveNetworkInfo:
        res = super().run()
        for nt in NetworkType:
            if nt.value in res:
                return ActiveNetworkInfo(network_type=nt, payload=res[nt.value])

        raise Exception('Could not find active network information entry')
