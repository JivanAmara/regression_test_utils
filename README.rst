==============
Test Utilities
==============

Test Utilities provides a decorator to automatically collect method
input & output to easily create regression tests for previously
untested code.

Quick Start (Assumes you have basic familiarity with python unittests)
-----------
* add this after your imports:
    from regression_test_utils import log_test_case
    import logging
    logger = logging.getLogger(__name__)

* add the decorator on the line before the method you want to collect from:
    @log_test_case(logger, __name__)
    def my_previously_untested_method(...):

* run your program, using features that use this method.

* Copy the TestCaseTemplate.py module to your tests directory and rename to something appropriate.

* In your test case module make the following updates:
  * from <my.module> import MyPreviouslyUntestedClass -> reflect your code
  * replace all instances of MyPreviouslyUntestedClass with your class' name.
  * If your class requires initilization arguments, update
      * test_instance = MyPreviouslyUntestedClass()

* Collect the jsonpickle'd test cases from your log file and in your test case module
  replace <my jsonpickle'd test cases> with them.
  (remember to add commas if there is more than one):
  * use grep -A1 MyPreviouslyUntestedClass.my_previously_untested_method \
        | grep -v Debug

Go ahead and run your tests.  You can now start your refactoring knowing you've got
a compass to keep you straight.

Additional Details
------------------
You'll probably want to update or inherit & override
TestMyPreviouslyUntestedClass.get_method_name() so that the method name
is a bit more descriptive in case of failure.
Currently it just includes the name of the method tested and the number
of args & kwargs.

