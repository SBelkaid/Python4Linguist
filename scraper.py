"""
Quick and dirty scraper. Not quick as in fast, but quickly written.
"""

import urllib
from bs4 import BeautifulSoup
import lxml.etree
import re 
import json
import time
import logging


logging.basicConfig(filename='logger.log',level=logging.DEBUG)

def retrieveLongLat(url):
	try:
		source = urllib.urlopen(url)
	except Exception, e:
		return
	logging.info("{} trying {}".format(time.strftime('%D %H:%M:%S'), url))
	if source.code == 200:
		markup = source.read()
		soup = BeautifulSoup(markup, 'lxml')
		el = soup.find('span', {'property': 'geo:geometry'})
		if el:
			key[url] = el.get_text()


def retrieveUrls(prog, data_dict):
	d = {}
	d[prog] = {}
	languages = data_dict[prog].keys()
	for l in languages:
		for author in data_dict[prog][l]:
			all_places = data_dict[prog][l][author]['all_dbp_urls_all_places']
			mother.extend(all_places)

if __name__=='__main__':
	crawled_urls = set()
	mother = []
	key = {}
	data = json.load(open('scripties.json'))
	for prog in data.keys():
		retrieveUrls(prog, data)
	for url in set(mother):
		retrieveLongLat(url)

	json.dump(key, open('lookUpDict.json', 'w+'))