from typing import Optional

from SCA11H.commands.base.PostCommand import PostCommand, PostResult
from SCA11H.commands.system.NetworkSecurityType import NetworkSecurityType

import json


class StationSettings:
    def __init__(self, ssid: str, security: NetworkSecurityType, dhcp_client_enabled: bool,
                 password: Optional[str] = None,
                 static_ip: Optional[str] = None, static_netmask: Optional[str] = None,
                 static_gateway: Optional[str] = None, static_dns_1: Optional[str] = None,
                 static_dns_2: Optional[str] = None):
        self.ssid = ssid
        self.security = security
        self.password = password
        self.dhcp_client_enabled = dhcp_client_enabled
        self.static_ip = static_ip
        self.static_netmask = static_netmask
        self.static_gateway = static_gateway
        self.static_dns_1 = static_dns_1
        self.static_dns_2 = static_dns_2

        if not self.dhcp_client_enabled and (
                self.static_ip is None or self.static_netmask is None or self.static_gateway is None or
                self.static_dns_1 is None or self.static_dns_2 is None):
            raise Exception('Disabled DHCP requires static network configuration parameters')

    def __str__(self):
        return self.to_json_string()

    def to_json_string(self):
        result = {
            'sta': {
                'ssid': self.ssid,
                'security': self.security.value,
                'passphrase': self.password,
                'dhcp': 1 if self.dhcp_client_enabled else 0,
            }
        }

        if not self.dhcp_client_enabled:
            result['sta']['ip'] = self.static_ip
            result['sta']['netmask'] = self.static_netmask
            result['sta']['gateway'] = self.static_gateway
            result['sta']['ipdns1'] = self.static_dns_1
            result['sta']['ipdns2'] = self.static_dns_2

        return json.dumps(result)


class SetNetworkSettings(PostCommand):
    """ Query Network Settings """

    def __init__(self, settings: StationSettings, **kwargs):
        super().__init__(endpoint='/sys/network', payload=settings.to_json_string(), **kwargs)

    def run(self, **kwargs) -> PostResult:
        return super().run()
