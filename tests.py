# -*- enconding: utf-8 -*-

import cminus_parser
import sys

if __name__ == '__main__':

	tests = ['examples/comments.c', 'examples/gcd.c',
			 'examples/fibonacci.c']
	cminus_parser.VERBOSE = 0	

	for test in tests:
		f = open(test, 'r')
		data = f.read()
		print 'test: ' + test + '..............\t',  
		try:
			cminus_parser.parser.parse(data, tracking=True)
			print '[ok]'
		except:
			print '[ko]'

