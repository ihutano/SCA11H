from SCA11H.commands.base.PostCommand import PostCommand
from SCA11H.commands.system.WiFiCountryCode import WiFiCountryCode


class SetWiFiCountryCode(PostCommand):
    """ Configure WiFi Country Code """

    def __init__(self, country: WiFiCountryCode, **kwargs):
        super().__init__(endpoint='/sys/country', payload='{"country":"%s"}' % country.value, **kwargs)
