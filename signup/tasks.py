from celery.task import Task
from signup.models import Signup


class SignupServiceCall(Task):
    queue = 'signup_service_call'

    def run(self, signup, **kwargs):
        logger = self.get_logger(**kwargs)
        assert type(signup) is Signup, \
            'signup is not a Signup instance (%s)' % \
        type(signup)

        print signup
        return True