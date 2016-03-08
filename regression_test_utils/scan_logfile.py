'''
Created on Mar 7, 2016

@author: jivan
'''
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
            re.findall('^(.*?Decorator TestCase.*?)$[\n\t]*?^(.*?)$', logfilecontent, flags=re.MULTILINE)
        for m in matches:
            if 'mhcii' not in m[0]: continue
            print('---')
            print(m[0])
            print(m[1])
