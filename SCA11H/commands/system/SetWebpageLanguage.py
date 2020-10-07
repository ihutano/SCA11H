from SCA11H.commands.base.PostCommand import PostCommand
from SCA11H.commands.system.WebpageLanguage import WebpageLanguage


class SetWebpageLanguage(PostCommand):
    """ Configure Webpage Language """

    def __init__(self, language: WebpageLanguage, **kwargs):
        super().__init__(endpoint='/sys/language', payload='{"language":"%s"}' % language.value, **kwargs)
