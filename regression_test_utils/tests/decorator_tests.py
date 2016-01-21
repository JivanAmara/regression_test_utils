'''
Created on Jan 20, 2016

@author: jivan
'''
from regression_test_utils import log_test_case
import logging
import os
from unittest import TestCase

logfilename = 'myloggingfile.log'
logfiledir = os.path.normpath(os.path.join(__file__, os.pardir))
logfilepath = os.path.join(logfiledir, logfilename)
logging.basicConfig(filename=logfilepath)
logger = logging.getLogger('mylogger')

class MyTestedClass(TestCase):
    def setup(self):
        # Initilize an empty log file, or truncate if it exists.
        with open(logfilepath, 'w+'):
            pass

#    @log_test_case(logger)
    def __init__(self, a, kw1=None, kw2=None):
        super(TestCase, self).__init__()

    @log_test_case(logger)
    def my_method(self, a, b):
        return 'ABC'

    def test_init_decoration(self):
        self.__init__(1, kw1='a', kw2='b')
        self.my_method('A', 'B')

        with open(logfilepath, 'r') as logfile:
            content = logfile.read()
            print(content)
