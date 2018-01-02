#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os, sys
import argparse
import urllib2
import codecs
import ssl

import colorama
import requests

from bs4 import BeautifulSoup as bs
from colorama import init
from colorama import Fore, Back, Style

init()

print ''
print Fore.RED + u'▒█▀▄▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ '
print Fore.RED + u'▒█▒█▒█ ▒█▄▄█ ▒█▄▄█ ▒█▄▄█ ▒█▀▀▀ ▒█▄▄▀ '
print Fore.RED + u'▒█░░▒█ ▒█░▒█ ▒█░░░ ▒█░░░ ▒█▄▄▄ ▒█░▒█ '
print Fore.RED + 'Written by hayzudev'
print ''

parser = argparse.ArgumentParser(description='Lightweight website mapper.')
parser.add_argument('-o','--output', help='Output file name', required=True)
parser.add_argument('-u','--url', help='Website url target', required=True)
args = vars(parser.parse_args())

_LINKS = []
_URL = args['url']
_OUTPUT = args['output']

if not _URL.startswith('http'):
	_URL = 'https://' + _URL

gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
request = urllib2.Request(_URL,headers={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)'})
html_page = urllib2.urlopen(request,context=gcontext)
soup = bs(html_page, "html.parser")

def extractLinks(element, elementRef, _RETURN):
	for i, link in enumerate(soup.findAll(element)):
		href = str(link.get(elementRef))
		if not href == 'None':
			if not href.startswith('http'):
				_RETURN.append(_URL + href)
			else:
				_RETURN.append(href)

extractLinks('a', 'href', _LINKS)
extractLinks('base', 'href', _LINKS)
extractLinks('link', 'href', _LINKS)
extractLinks('script', 'src', _LINKS)
extractLinks('a', 'href', _LINKS)

file = codecs.open(_OUTPUT, 'w', encoding='utf-8') 
file.write('')
file.write(u'▒█▀▄▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ \n')
file.write(u'▒█▒█▒█ ▒█▄▄█ ▒█▄▄█ ▒█▄▄█ ▒█▀▀▀ ▒█▄▄▀ \n')
file.write(u'▒█░░▒█ ▒█░▒█ ▒█░░░ ▒█░░░ ▒█▄▄▄ ▒█░▒█ \n')
file.write('')
for l in _LINKS:
	print Fore.GREEN + '[+] ' + Fore.WHITE + l
	file.write(l + '\n') 
file.close()

print
print Fore.RED + '[!] ' + str(len(_LINKS)) + ' results found'
print