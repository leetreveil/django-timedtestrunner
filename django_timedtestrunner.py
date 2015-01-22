import time

from django.test.runner import DiscoverRunner
from django.utils.unittest import TextTestResult, TextTestRunner


class TimedTestRunner(DiscoverRunner):

    def run_suite(self, suite, **kwargs):
        return TimedTextTestRunner(verbosity=self.verbosity, failfast=self.failfast).run(suite)


class TimedTestResult(TextTestResult):

    test_times = []

    def startTest(self, test):
        self.start_time = time.time()
        super(TimedTestResult, self).startTest(test)

    def addSuccess(self, test):
        time_taken = time.time() - self.start_time
        self.test_times.append((time_taken, str(test)))
        super(TimedTestResult, self).addSuccess(test)


class TimedTextTestRunner(TextTestRunner):
    resultclass = TimedTestResult

    def run(self, test):
        result = super(TimedTextTestRunner, self).run(test)

        num_tests_to_print = 5

        self.stream.write('\n')
        self.stream.writeln('Top %d slowest tests:' % num_tests_to_print)
        topn = sorted(result.test_times, reverse=True)[:num_tests_to_print]
        map(self.stream.writeln, ['(%0.3fs) %s' % s for s in topn])
        self.stream.write('\n')

        return result
