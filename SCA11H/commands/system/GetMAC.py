from SCA11H.commands.base.GetCommand import GetCommand


class GetMAC(GetCommand):
    """ Query Device MAC Address """

    def __init__(self, **kwargs):
        super().__init__(endpoint='/sys/mac', **kwargs)

    def run(self, **kwargs) -> str:
        return super().run()['mac']
