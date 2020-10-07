from SCA11H.commands.base.PostCommand import PostCommand
import json
import sys


class SetHTTPPassword(PostCommand):
    """ Configure Authentication Account """

    def __init__(self, old_password: str, new_password: str, **kwargs):
        super().__init__(endpoint='/sys/account',
                         payload=json.dumps({"password": old_password, "new_password": new_password}),
                         **kwargs)

        if len(old_password.encode('ascii')) > 16:
            raise Exception('Maximal old password length is 32 bytes')

        if len(new_password.encode('ascii')) > 16:
            raise Exception('Maximal new password length is 32 bytes')

        print("WARNING: SetHTTPPassword didn't work upon testing and always returned -1", file=sys.stderr)
