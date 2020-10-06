from SCA11H.commands.base.GetCommand import GetCommand
from SCA11H.commands.system.NetworkSecurityType import NetworkSecurityType


class SettingsEntry:
    def __init__(self, payload):
        self.ssid = payload['ssid']
        self.security = NetworkSecurityType.from_string(payload['security'])
        self.password = payload['passphrase']
        self.channel = payload.get('channel', 11)
        self.dhcp_client_enabled = payload.get('dhcp', None)
        self.dhcp_server_enabled = payload.get('dhcpd', None)
        self.static_ip = payload.get('ip', None)
        self.static_netmask = payload.get('netmask', None)
        self.static_gateway = payload.get('gateway', None)
        self.static_dns_1 = payload.get('ipdns1', None)
        self.static_dns_2 = payload.get('ipdns2', None)

    def __str__(self):
        result = {
            'ssid': self.ssid,
            'security': self.security.value,
            'password': self.password,
            'channel': self.channel,
        }

        def add_field(name, value):
            if value is not None:
                nonlocal result
                result[name] = value

        add_field('dhcp_client_enabled', self.dhcp_client_enabled)
        add_field('dhcp_server_enabled', self.dhcp_server_enabled)
        add_field('static_ip', self.static_ip)
        add_field('static_netmask', self.static_netmask)
        add_field('static_gateway', self.static_gateway)
        add_field('static_dns_1', self.static_dns_1)
        add_field('static_dns_2', self.static_dns_2)

        return '%s' % result

    def __repr__(self):
        return '%s' % self.__str__()


class SettingsBundle:
    def __init__(self, payload):
        self.soft_ap = SettingsEntry(payload=payload['ap'])
        self.station = SettingsEntry(payload=payload['sta'])

    def __str__(self):
        res = {
            'soft_ap': self.soft_ap,
            'station': self.station
        }
        return '%s' % res


class GetNetworkSettings(GetCommand):
    """ Query Network Settings """

    def __init__(self, **kwargs):
        super().__init__(endpoint='/sys/network', **kwargs)

    def run(self, **kwargs) -> SettingsBundle:
        return SettingsBundle(payload=super().run())
