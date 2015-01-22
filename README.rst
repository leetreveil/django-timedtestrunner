django-timedtestrunner
-----

Displays a summary of your slowest tests after your test run has finished:

.. code:: bash

    Creating test database for alias 'default'...
    .....
    ----------------------------------------------------------------------
    Ran 5 tests in 160.597s

    OK

    Top 5 slowest tests:
    (90.200s) test_speed_of_coral (slowanimals.tests.TestSlowAnimals)
    (25.297s) test_speed_of_snail (slowanimals.tests.TestSlowAnimals)
    (14.893s) test_speed_of_sloth (slowanimals.tests.TestSlowAnimals)
    (12.851s) test_speed_of_tortoise (slowanimals.tests.TestSlowAnimals)
    (10.828s) test_speed_of_spider (slowanimals.tests.TestSlowAnimals)

    Destroying test database for alias 'default'...

Install
-----

::

    pip install -e git://github.com/django-timedtestrunner/django-timedtestrunner.git#egg=django-timedtestrunner

Then just set ``TEST_RUNNER`` in ``settings.py`` and you are good to go!

.. code:: python

    TEST_RUNNER = 'django_timedtestrunner.TimedTestRunner'

Licence
----
MIT