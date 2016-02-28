"""
generates KML files for visualization. 
"""

import urllib
from bs4 import BeautifulSoup
import lxml.etree
import re 
import json
import time
import logging
import lxml.etree
import os
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import GX_ElementMaker as GX
from collections import defaultdict


OUTPUT_FOLDER = 'kml_files/'

def constructKML(urls, course_name):
	doc = GX.kml()
	for url in urls:
		# print url #see if it prints urls 
		name = url.split('/')[-1]
		point = points_dict.get(url)
		if point:
			langt, longt = point.strip('POINT()').split(' ')
			pm = GX.Placemark(
				GX.name(name),
				GX.Point(
					GX.coordinates(langt + ',' + longt))
				)
			doc.append(pm)
	xml = lxml.etree.tostring(doc, pretty_print=True, xml_declaration=True)
	with open(OUTPUT_FOLDER+course_name+'.kml', 'w') as f:
		f.write(xml)

def retrieveUrls(prog, data_dict):
	urls = set()
	languages = data_dict[prog].keys()
	for l in languages:
		for author in data_dict[prog][l]:
			#could also be something else instead of only locations
			all_places = data_dict[prog][l][author]['all_dbp_urls_all_places']
			urls.update(all_places)
	constructKML(urls, prog)

if __name__=='__main__':
	points_dict = json.load(open('lookUpDict.json', 'r'))
	data = json.load(open('scripties.json'))
	if not os.path.isdir(OUTPUT_FOLDER):
		os.mkdir(OUTPUT_FOLDER)

	# retrieveUrls('erf', data) #exute only one

	for prog in data.keys():
		retrieveUrls(prog, data)