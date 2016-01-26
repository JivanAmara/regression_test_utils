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


class log_function_call(object):
    def __init__(self, logger):
        self.logger = logger

    def __call__(self, func):
        def wrapped_func(*args, **kwargs):
            result = func(*args, **kwargs)
            # The instance the function belongs to.  None for unbound methods or functions
            #    outside of classes.
            func_instance = func.__self__ if hasattr(func, '__self__') else None
            func_class = func_instance.__class__ if func_instance else None

            # If it's a bound method, strip the 'self' arg.
            if hasattr(func, '__self__') and func.__self__ is not None:
                args_wo_instance = args[1:]
            else:
                args_wo_instance = args

            jsonp_test = repr(
                jsonpickle.encode(
                    (func.__name__, args_wo_instance, kwargs, result), keys=True
                )
            )
            self.logger.debug('Method Decorator Test for "{class_}.{func} ({id})":\n\t{test}'\
                .format(**{
                    'class_': func_class,
                    'func': func.__name__,
                    'id': None if not func_instance else id(func_instance),
                    'test': jsonp_test,
                })
            )

            return result

        return wrapped_func

# class LoggingMetaClass(type):
#     ''' @brief: MetaClass which logs all use of instances of the class using this MetaClass.
#         @author: Jivan
#         @since: 2016-01-26
#     '''
#     def __new__(cls, name, bases, attrs):
#
#
# class log_instance_usage(object):
#     ''' @brief: Class decorator which logs all calls to each instance of a class in order to
#             automatically create tests.
#         @author: Jivan
#         @since: 2016-01-25
#     '''
#     def __init__(self, logger):
#         self.logger = logger
#
#     def __call__(self, WrappedClass):
#         o = WrappedClass
