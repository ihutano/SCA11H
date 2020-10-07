from enum import Enum


class WebpageLanguage(Enum):
    English = 'en'
    Chinese = 'zh'

    @staticmethod
    def from_string(text: str):
        for t in WebpageLanguage:
            if t.value == text:
                return t

        raise Exception('Unexpected webpage language: %s' % text)
