from enum import Enum
import json

from SCA11H.commands.base.PostCommand import PostCommand


class Command(Enum):
    Reboot = 'reboot'  # Reboots the system
    Restore = 'restore'  # Restore system's factory settings and reboot the system


class RunCommand(PostCommand):
    """ Run a system command """

    def __init__(self, command: Command, **kwargs):
        super().__init__(endpoint='/sys/cmd',
                         payload=json.dumps({"cmd": command.value}),
                         **kwargs)
