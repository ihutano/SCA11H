from SCA11H.commands.base.GetCommand import GetCommand
from SCA11H.commands.system.WebpageLanguage import WebpageLanguage


class GetWebpageLanguage(GetCommand):
    """ Query Webpage Language """

    def __init__(self, **kwargs):
        super().__init__(endpoint='/sys/language', **kwargs)

    def run(self, **kwargs) -> WebpageLanguage:
        return WebpageLanguage.from_string(super().run()['language'])
