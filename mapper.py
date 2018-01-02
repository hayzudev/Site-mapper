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

INIT_TEXT =  '\n' + u'▒█▀▄▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ \n' + u'▒█▒█▒█ ▒█▄▄█ ▒█▄▄█ ▒█▄▄█ ▒█▀▀▀ ▒█▄▄▀ \n' + u'▒█░░▒█ ▒█░▒█ ▒█░░░ ▒█░░░ ▒█▄▄▄ ▒█░▒█ \n' + Fore.WHITE + '-> Written by hayzu.'
print Fore.RED + INIT_TEXT

_PARSER = argparse.ArgumentParser(description='Lightweight website mapper.')
_PARSER.add_argument('-t','--target', help='Target Url.', required=True)
_PARSER.add_argument('-o','--output', help='Output file name.', required=False)
_ARGS = vars(_PARSER.parse_args())
_TARGET = _ARGS['target']
_OUTPUT = _ARGS['output']

if not _TARGET.startswith('http'): _TARGET = 'https://' + _TARGET;

_REQUEST = urllib2.Request(_TARGET, headers={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)'})
_HTMLCODE = urllib2.urlopen(_REQUEST, context=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2))
_SOUP = bs(_HTMLCODE, "html.parser")

def collect_links(element, object, array):
	for i, link in enumerate(_SOUP.findAll(element)):
		href = str(link.get(object))
		if not href in _LINKS:
			if href != '#':
				if href != 'None':
					if not href.startswith('http'):
						array.append(_TARGET + href)
					else:
						array.append(href)

_LINKS = []
_IMGLINKS = []
_ELEMENTS = { 'a': 'href', 'base': 'href', 'link': 'href', 'script': 'src' }

for x in _ELEMENTS:
	collect_links(x, _ELEMENTS[x], _LINKS)
collect_links('img', 'src', _IMGLINKS)

if not _OUTPUT is None:
	file = codecs.open(_OUTPUT, 'w', encoding='utf-8') 
	file.write(INIT_TEXT)
	for l in _LINKS:
		print Fore.GREEN + '[+] ' + Fore.WHITE + l
		file.write(l + '\n') 
	if _IMGLINKS != None:
		print Fore.ORANGE + '-> Images: '
		for l in _IMGLINKS:
			file.write(l + '\n') 
			print Fore.GREEN + ' [+] ' + Fore.WHITE + l
	file.close()
else:
	for l in _LINKS:
		print Fore.GREEN + '[+] ' + Fore.WHITE + l
	if _IMGLINKS != None:
		print Fore.CYAN + '-> Images: '
		for l in _IMGLINKS:
			print Fore.GREEN + ' [+] ' + Fore.WHITE + l
print Fore.RED + '\n[!] ' + str(len(_LINKS)) + ' results found\n'
