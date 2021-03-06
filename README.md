# Installation

`mysite/settings.py` is missing from this project. Please create your own.

# Testing

To run tests and find out the coverage run the following:

```bash
➫ coverage run --omit="*/migrations/*,*/tests/*,*/.virtualenvs/*" \
manage.py test polls signup; \
coverage report; coverage annotate
```

You should see an output like the following:

```bash
Creating test database for alias 'default'...
.............
----------------------------------------------------------------------
Ran 13 tests in 0.143s

OK
Destroying test database for alias 'default'...
Name              Stmts   Miss  Cover
-------------------------------------
manage                6      0   100%
mysite/__init__       0      0   100%
mysite/settings      27      0   100%
mysite/urls           7      0   100%
polls/__init__        0      0   100%
polls/admin           7      0   100%
polls/models         17      1    94%
polls/tests          51      0   100%
polls/urls            7      0   100%
polls/views          28      8    71%
signup/__init__       0      0   100%
signup/admin          9      1    89%
signup/models        61      9    85%
signup/tests         18      0   100%
signup/urls           3      0   100%
signup/views         36      9    75%
-------------------------------------
TOTAL               277     28    90%
```

# Code quality

To check for PEP-8 compliance:

```bash
➫ find . | grep .py$ | grep -v '._' | xargs pep8
```

# Tasks

```bash
➫ python manage.py celeryd \
--concurrency=2 --autoscale=3,2 \
--verbosity=3 --loglevel=INFO \
--queues=signup_service_call \
-n signup_service_call
```

Example usage:

```python
from signup.tasks import SignupServiceCall
from signup.models import Signup

signup = Signup.objects.all()[0]
task = SignupServiceCall()
for i in range(0, 1000):
    task.delay(signup)
```