from SCA11H.commands.base.PostCommand import PostCommand, PostResult


class SetAlias(PostCommand):
    """ Configure BSN Name """

    def __init__(self, name: str, **kwargs):
        super().__init__(endpoint='/sys', payload='{"alias":"%s"}' % name, **kwargs)
        if len(name.encode('ascii')) > 32:
            raise Exception('Maximal name length is 32 bytes')

    def run(self, **kwargs) -> PostResult:
        return super().run()
