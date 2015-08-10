'''
Created on Aug 4, 2015

@author: jivan
'''

import jsonpickle
from unittest import TestCase

from <my.module> import MyPreviouslyUntestedClass

jp_test_cases = [
    <my jsonpickle'd test cases>
]

class TestMyPreviouslyUntestedClass(TestCase):
    TestClass = MyPreviouslyUntestedClass
    test_instance = MyPreviouslyUntestedClass()

    @classmethod
    def get_method_name(cls, idx, method_args, method_kwargs):
        method_name, sequences, allele_lengths_list = method_args
	# Dynamically created method name
        mn = 'test_{:02}_{}_args_{}_kwargs_{}'.format(
                    idx, method_name, len(method_args), len(method_kwargs))
        return mn

    def perform_one_tc(self, tc):
        tested_method_name = tc[0]
        args = tc[1]
        kwargs = tc[2]
        expected_result = tc[3]

        result = getattr(self.test_instance, tested_method_name)(*args, **kwargs)
        self.assertEqual(result, expected_result)

    @classmethod
    def _add_method(cls, method_name, testcase):
        """ @brief: This is used to add a separate method for each of the test cases so they
                run individually instead of en masse.
        """
        def new_test_method(self, tc=testcase):
            self.perform_one_tc(tc)

        new_method.__name__ = method_name
        from types import MethodType
        m = MethodType(new_method, None, cls)
        setattr(cls, method_name, m)

for i, jp_testcase in enumerate(jp_test_cases):
    test_case = jsonpickle.decode(jp_testcase, keys=True)
    tested_method_args = test_case[1]
    tested_method_kwargs = test_case[2]
 
    test_method_name = \
        TestMyPreviouslyUntestedClass.get_method_name(i, tested_method_args, tested_method_kwargs)
    TestMyPreviouslyUntestedClass._add_method(test_method_name, test_case)
