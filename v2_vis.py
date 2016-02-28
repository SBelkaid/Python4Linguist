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
		print url
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
	d = defaultdict(set)
	d[prog]
	languages = data_dict[prog].keys()
	for l in languages:
		for author in data_dict[prog][l]:
			all_places = data_dict[prog][l][author]['all_dbp_urls_all_places']
			d[prog].update(all_places)
	constructKML(d[prog], prog)


points_dict = json.load(open('lookUpDict.json', 'r'))
data = json.load(open('scripties.json'))
if not os.path.isdir(OUTPUT_FOLDER):
	os.mkdir(OUTPUT_FOLDER)

# retrieveUrls('erf', data)

for prog in data.keys():
	retrieveUrls(prog, data)