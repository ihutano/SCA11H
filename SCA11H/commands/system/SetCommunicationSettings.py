from SCA11H.commands.base.PostCommand import PostCommand
from SCA11H.commands.system.CommunicationSettings import CommunicationSettings


class SetCommunicationSettings(PostCommand):
    """ Configure Communication Settings """

    def __init__(self, settings=CommunicationSettings, **kwargs):
        super().__init__(endpoint='/sys/comm', payload='%s' % settings, **kwargs)
