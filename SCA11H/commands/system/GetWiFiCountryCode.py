from SCA11H.commands.base.GetCommand import GetCommand
from SCA11H.commands.system.WiFiCountryCode import WiFiCountryCode


class GetWiFiCountryCode(GetCommand):
    """ Query WiFi Country Code """

    def __init__(self, **kwargs):
        super().__init__(endpoint='/sys/country', **kwargs)

    def run(self, **kwargs) -> WiFiCountryCode:
        return WiFiCountryCode.from_string(super().run()['country'])
