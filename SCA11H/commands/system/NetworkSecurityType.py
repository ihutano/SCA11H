from enum import Enum


class NetworkSecurityType(Enum):
    Open = 'Open'
    WEP = 'WEP'
    WPA2_PSK = 'WPA2 PSK'
    WPA = 'WPA/WPA2 PSK'
    Unknown = 'Unknown'

    @staticmethod
    def from_string(text: str):
        for t in NetworkSecurityType:
            if t.value == text:
                return t

        raise Exception('Unexpected security type: %s' % text)
