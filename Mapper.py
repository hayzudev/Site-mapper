#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
import os, sys
import requests
import urllib2
import codecs
import ssl

print ''
print u'▒█▀▄▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ '
print u'▒█▒█▒█ ▒█▄▄█ ▒█▄▄█ ▒█▄▄█ ▒█▀▀▀ ▒█▄▄▀ '
print u'▒█░░▒█ ▒█░▒█ ▒█░░░ ▒█░░░ ▒█▄▄▄ ▒█░▒█ '
print ''

_LINKS = []
_URL = sys.argv[1]
_OUTPUT = sys.argv[2]

if not _URL.startswith('http'):
	_newURl = 'https://' + _URL
	_URL = _newURl

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
	print '[+] -> ' + l
	file.write(l + '\n') 
file.close()

print '[!] ' + str(len(_LINKS)) + ' Founds Finished'
