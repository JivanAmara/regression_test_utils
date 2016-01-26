'''
Created on Jan 25, 2016

@author: jivan
'''
import StringIO
import logging
import unittest

from regression_test_utils.regression_test_utils import log_function_call


class TestFunctionCallLoggingDecorator(unittest.TestCase):
    # in-memory log file
    memlogfile = StringIO.StringIO()
    logger = logging.getLogger('function_decorator_logger')
    logger.addHandler(logging.StreamHandler(stream=memlogfile))
    logger.setLevel(logging.DEBUG)

    def test_simple(self):
        @log_function_call(logger=self.logger)
        def simple(a, b):
            return a + b

        simple(1, 2)
        log_contents = self.memlogfile.getvalue()
        self.memlogfile.close()
        self.fail(log_contents.strip())

if __name__ == '__main__':
    unittest.main()
