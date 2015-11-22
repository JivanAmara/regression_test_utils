from regression_test_utils import log_test_case
import logging
logger = logging.getLogger(__name__)

logging.basicConfig(filename='test_log.log', level=logging.DEBUG)

class test_program(object):

	@log_test_case(logger, __name__)
	def combine(method_name, log_file):
		result = method_name + " " + log_file
		return result;

	combine('my_method,', 'results')
