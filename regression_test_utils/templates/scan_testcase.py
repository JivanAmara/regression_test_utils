import jsonpickle
from {classmodule} import {classname}
import unittest

class {classname}Tests(unittest.TestCase):
    def test_basic(self):
        jp_init = '{jp_initdetails}'
        jp_testdetails = '{jp_testdetails}'

        ignored_methodname, args, kwargs, ignored_result = jsonpickle.decode(jp_init, keys=True)
        o = {classname}(*args, **kwargs)

        methodname, args, kwargs, expected_result = jsonpickle.decode(jp_testdetails, keys=True)
        result = o.{methodname}(*args, **kwargs)
        
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
