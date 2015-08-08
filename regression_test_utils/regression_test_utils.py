'''
Created on Jul 29, 2015

@author: jivan
'''
import jsonpickle, logging

# PythonDecorators/my_decorator.py
class log_test_case(object):
    """ @brief: Decorator to log input & output of a method as a jsonpickle'd tuple for easy
            test creation.
        Format of the tuple is (<method name>, <args (without self)>, <kwargs>, <result>)
        @author: Jivan
        @since: 2015-07-29
        @change: 2015-08-03 by Jivan: Added class_name to initialization & logged output.
    """
    def __init__(self, logger, class_name):
        self.logger = logger
        self.class_name = class_name

    def __call__(self, f):
        method_name = f.__name__
        logger = self.logger
        def wrapped_f(*args, **kwargs):
            result = f(*args, **kwargs)
            if logger.getEffectiveLevel() <= logging.DEBUG:
                args_wo_instance = args[1:]
                tc = repr(jsonpickle.encode(
                            (method_name, args_wo_instance, kwargs, result), keys=True
                          )
                     )
                logger.debug('Decorator TestCase for "{}.{}":\n\t{}'\
                                 .format(self.class_name, method_name, tc))
            return result
        return wrapped_f
