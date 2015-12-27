from regression_test_utils import log_test_case
import logging
logger = logging.getLogger(__name__)

logging.basicConfig(filename='test_log.log', level=logging.DEBUG)

class TestClass(object):

	@log_test_case(logger, __name__)
	def combine(self, method_name, log_file):
		result = method_name + " " + log_file
		return result;

if __name__ == '__main__':
	tc = TestClass()
	tc.combine('my_method,', 'results')
	tc.combine('hello,', 'my friend')