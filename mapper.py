#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import codecs
import argparse
import requests
import lxml.html
from colorama import init
from colorama import Fore

init()
inittext = '\n' + u'▒█▀▄▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ \n'  + u'▒█▒█▒█ ▒█▄▄█ ▒█▄▄█ ▒█▄▄█ ▒█▀▀▀ ▒█▄▄▀ \n' + u'▒█░░▒█ ▒█░▒█ ▒█░░░ ▒█░░░ ▒█▄▄▄ ▒█░▒█ \n' + Fore.WHITE + '-> Written by hayzu.\n'
print inittext

parser = argparse.ArgumentParser(description='Lightweight website mapper.')
parser.add_argument('-t','--target', help='Target Url.', required=True)
parser.add_argument('-o','--output', help='Output file name.', required=False)

args = vars(parser.parse_args())
target = args['target']
output = args['output']

try:
	r = requests.get(target, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'})
	dom = lxml.html.fromstring(r.text)
except:
	print  Fore.RED + '[-]' + Fore.WHITE + ' invalid url try: https://www.example.com' 
	sys.exit()
links = []

if not output is None:
	file = codecs.open(output, 'w', encoding='utf-8') 
	file.write(inittext.replace('[37m', '') + '\n')
	file.write('')

def extract(a,b):
	for link in dom.xpath('//' + a + '/@' + b):
		if link.startswith('/'):
			link = target + link
			print Fore.GREEN + '[+] ' + Fore.WHITE + link
			if not output is None:
				file.write(link + '\n') 
		else:
			print Fore.GREEN + '[+] ' + Fore.WHITE +  link
			if not output is None:
				file.write(link + '\n')
		links.append(link)

extract('img', 'src')
extract('a', 'href')
extract('link', 'href')

print '\n' + Fore.RED + '[!] ' + Fore.WHITE + str(len(links)) + ' results found\n'
