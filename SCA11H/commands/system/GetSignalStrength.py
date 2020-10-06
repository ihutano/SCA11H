from SCA11H.commands.base.GetCommand import GetCommand


class GetSignalStrength(GetCommand):
    """ Query Network RSSI """

    def __init__(self, **kwargs):
        super().__init__(endpoint='/sys/rssi', **kwargs)

    def run(self, **kwargs) -> int:
        return int(super().run()['rssi'])
