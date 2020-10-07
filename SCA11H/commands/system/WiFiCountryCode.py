from enum import Enum


class WiFiCountryCode(Enum):
    US = 'US'
    Japan = 'JP'
    Europe = 'EU/CN'

    @staticmethod
    def from_string(text: str):
        for t in WiFiCountryCode:
            if t.value == text:
                return t

        raise Exception('Unexpected WiFi country code: %s' % text)
