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
    def __init__(self, logger):
        self.logger = logger

    def __call__(self, f):
        method_class = f.__class__
        method_name = f.__name__
        logger = self.logger
        def wrapped_f(*args, **kwargs):
            result = f(*args, **kwargs)
            if logger.getEffectiveLevel() <= logging.DEBUG:
                args_wo_instance = args[1:]
                jsonp_test = repr(jsonpickle.encode(
                            (method_name, args_wo_instance, kwargs, result), keys=True
                          )
                     )
                logger.debug('Method Decorator Test for "{}.{}":\n\t{}'\
                                 .format(method_class, method_name, jsonp_test))
            return result
        return wrapped_f
