'''
Created on Mar 7, 2016

@author: jivan
'''
from __future__ import unicode_literals
from argparse import ArgumentParser
import re


if __name__ == '__main__':
    ap = ArgumentParser(description='Scan the specified log file for logged regression tests')
    ap.add_argument('logfilename', help='Name of the log file to scan for logged regression tests')
    args = ap.parse_args()
    print('Collecting regression tests from "{}".'.format(args.logfilename))
    with open(args.logfilename) as lf:
        logfilecontent = lf.read()
        newline_matches = re.findall('\n', logfilecontent)
        print('Log file has {} lines'.format(len(newline_matches)))
        matches = \
            re.findall('^(.*?Decorator TestCase.*?)$[\n\t]*?^\s*\'(.*?)\'\s*$', logfilecontent, flags=re.MULTILINE)

        tests = []
        for m in matches:
            if 'mhcii' not in m[0]: continue
            header_line = m[0]
            classmethod_regex = r'^.*?Decorator TestCase for "(.*?)":'
            search_result = re.search(classmethod_regex, header_line)
            if not search_result: raise Exception("Couldn't find a testcase in log extract")
            class_method_details = search_result.group(1)
            split_details = class_method_details.split('.')
            classdottedpath = '.'.join(split_details[:-1])
            classmodule = '.'.join(split_details[:-2])
            classname = split_details[-2]
            methodname = split_details[-1]
            jsonpickled_io = m[1].strip()

            tests.append({
                'classdottedpath': classdottedpath, 'classmodule': classmodule,
                'classname': classname, 'methodname': methodname,
                'jsonpickledio': jsonpickled_io
            })

        # These are groups of tests that apply to the same instance.
        # Groups are deliniated by calls to __init__().
        open_testgroups = {}
        closed_testgroups = []
        for test in tests:
            classdottedpath = test['classdottedpath']
            methodname = test['methodname']
            # If we've got an __init__ call after already seeing calls to an instance of this
            #    class, start a new test group for the new instance.
            # TODO: This works for now, but won't survive interleaved logging of test cases
            #    for instances whose timelines overlap.
            if methodname == '__init__' and classdottedpath in open_testgroups:
                closed_testgroups.append(open_testgroups.pop(classdottedpath))
            if classdottedpath not in open_testgroups:
                open_testgroups[classdottedpath] = []
            open_testgroups[classdottedpath].append(test)
        otg_keys = open_testgroups.keys()
        for classdottedpath in otg_keys:
            closed_testgroups.append(open_testgroups.pop(classdottedpath))

        print('total tests: {}'.format(len(tests)))
        print('test groups: {}'.format(len(closed_testgroups)))

        import importlib
        with open('regression_test_utils/templates/scan_testcase.py') as tf:
            template_content = tf.read()

        for i, tg in enumerate(closed_testgroups):
            context = {}
            for tc in tg:
                classmodule = tc['classmodule']
                classname = tc['classname']
                methodname = tc['methodname']
                jsonpicklestring = tc['jsonpickledio']

                context['{classmodule}'] = classmodule
                context['{classname}'] = classname
                context['{methodname}'] = methodname
                if methodname == '__init__':
                    context['{jp_initdetails}'] = jsonpicklestring
                else:
                    context['{jp_testdetails}'] = jsonpicklestring

            test_code = template_content
            if context:
                for old, new in context.items():
                    test_code = test_code.replace(old, new)
                with open('autotests/{}Tests-{}.py'.format(classname, i), 'w') as testfile:
                    testfile.write(test_code)
