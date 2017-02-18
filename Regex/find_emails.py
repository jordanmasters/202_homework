import re
import sys
import logging

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)


if __name__ == '__main__':
	logging.info('Reading File...')
	data = sys.stdin.read()

	email_pattern = r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,5})'

	matches = re.findall(email_pattern, data)
	
	# In reality one would probably want to output this to a file or variable somewhere, 
	# but for now, just the print, since im not sure what to use this for at the moment
	for match in matches:
		print match
	print len(matches), 'Matches'
	
	logging.info('Done.')
else:
	# if you try to import me ...
	logging.error('This program takes a file in std in, run me from the command line - python find_emails.py < myfile.txt')



