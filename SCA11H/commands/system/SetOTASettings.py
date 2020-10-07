from SCA11H.commands.base.PostCommand import PostCommand
from SCA11H.commands.system.OTASettings import OTASettings


class SetOTASettings(PostCommand):
    """ Configure OTA Settings """

    def __init__(self, settings: OTASettings, **kwargs):
        super().__init__(endpoint='/sys/ota', payload=settings.to_payload(), **kwargs)
