"""
Parser, extracts data from KAF NAF files.
"""
import fnmatch
import operator
import os
import lxml.etree
import logging
from nltk import FreqDist
from nltk.corpus import stopwords
from collections import defaultdict
from datetime import datetime
import json


STOPWORDS = stopwords.words('dutch')
STOPWORDS.extend(stopwords.words('english'))
DIR_NAME = 'thesis_vu_2015'
PATTERN = '*.nohyphen'
logging.basicConfig(filename='logger.log',level=logging.DEBUG)

def split_path(e):
	splitted = e.split('/')
	prog_lang = splitted[1:-1]
	name = splitted[-1]
	return splitted, prog_lang, name

def trav(d, l, p, data=None):
	"""
	:param folder structure, program language (en, nl), author name,
	optional parameter for the data dictionairy generated by ectractor.
	Recursinve function needed for traversing original folder structure dictionairy
	"""
	i = iter(l)
	r = d[i.next()]
	if isinstance(r,dict):
		try:
			trav(r, [i.next()], p, data)
		except StopIteration, e:
			r[p] = data

def reconstructFolderStruct(directories):
	d = [i for i in directories if i]
	q = {}
	for i in range(len(d[0])):
		q[d[0][i]] = defaultdict(dict)
		for lang in d[i+1]:
			q[d[0][i]][lang] = defaultdict(dict)
	return q

def loadData(dir_name, pattern):
	"""
	finds files based on the defined extension (pattern param)
	"""
	nohyphen_files = []
	dir_names = []
	dir_paths = []
	for root, dirnames, filenames in os.walk(dir_name):
		dir_names.append(dirnames)
		dir_paths.append(root)
		for filename in fnmatch.filter(filenames, pattern):
			nohyphen_files.append(os.path.join(root, filename))
	return nohyphen_files, dir_names, dir_paths

def freq(element_list, descending=True):
	agglomerated = defaultdict(int)
	for e in element_list:
		agglomerated[e] += 1
	return sorted(agglomerated.items(), key=operator.itemgetter(1), reverse=descending)

def lexDiv(amount_words):
	return 1.0*len(set(amount_words))/len(amount_words)

def anotherFreq(list_types, list_words):
	"""
	returns 10 most frequent types and 10 most frequent words
	"""
	fd = FreqDist(list_types)
	agglomerated = defaultdict(int)
	for w in list_words:
		if not w.lower() in STOPWORDS:
			agglomerated[w] += 1
	sorted_dict = sorted(agglomerated.items(), key=operator.itemgetter(1), reverse=True)
	return sorted_dict[:10], [t for t, freq in fd.items()[:10]]

def extractor(f):
	"""
	:param path to file
	Adds data parsed from the KAF NAF files with the author as key 
	to a dictionairy containing	the reconstructed folder structure.
	"""
	logging.info("parsing file: {}".format(f))
	try:
		# doc = lxml.etree.ElementTree(lxml.etree.XML(f))
		doc = lxml.etree.ElementTree(file=f)
	except lxml.etree.XMLSyntaxError, e:
		logging.error(e)
		return
	doc_evaluator = lxml.etree.XPathEvaluator(doc)
	entities = doc_evaluator('//entity/*/externalRef/@reference')
	places_dbpedia = doc_evaluator('//entity[contains(@type, "Schema:Place")]/*/externalRef/@reference')
	non_people_dbpedia = doc_evaluator('//entity[not(contains(@type, "Schema:Person"))]')
	people = doc_evaluator('//entity[contains(@type, "Schema:Person")]/*/externalRef/@reference')
	words = doc.xpath('text/wf[re:match(text(), "[A-Za-z-]")]/text()',\
	 	namespaces={"re": "http://exslt.org/regular-expressions"})
	unique_words = set(words)
	other_tokens = doc.xpath('text/wf[re:match(text(), "[^A-Za-z-]")]/text()',\
	 	namespaces={"re": "http://exslt.org/regular-expressions"})
	amount_of_sentences = doc_evaluator('text/wf/@sent')[-1]
	types = doc_evaluator('//term/@morphofeat')
	longest_sentence = freq(doc.xpath('text/wf[re:match(text(), "[A-Za-z-]")]/@sent',\
		namespaces={"re": "http://exslt.org/regular-expressions"}))[0]

	top_people = freq([e.split('/')[-1] for e in people])[:10]
	top_entities = freq([e.split('/')[-1] for e in entities])[:10]
	top_places = freq([e.split('/')[-1] for e in places_dbpedia])[:10]
	most_freq_types, most_freq_words = anotherFreq(types, words)

	#stats from xml parse
	data = {
	'ten_most_frequent_people': top_people,
	'ten_most_frequent_entities': top_entities,
	'ten_most_frequent_places': top_places,
	'ten_most_frequent_types': most_freq_types,
	'most_freq_words': most_freq_words,
	'Amount_of_words': len(words),
	'amount_unique_words': len(other_tokens),
	'lexical_diversity': lexDiv(words),
	'amount_of_other_tokens': len(unique_words),
	'amount_of_sentences': amount_of_sentences,
	'amount_of_non_people_dbpedia': len(non_people_dbpedia),
	'amount_of_people mentioned': len(set(people)),
	'amount_of_locations': len(set(places_dbpedia)),
	'amount_of_types': len(types),
	'longest_sentence': longest_sentence[1],
	'longest_sentence_number': longest_sentence[0],
	'all_dbp_urls_all_places': places_dbpedia,
	'all_words': list(words),
	'all_people': people,
	# 'all_non_people_dbp': list(non_people_dbpedia),
	'all_entities': entities}

	splitted, prog_lang, name = split_path(f)
	trav(q, prog_lang, name, data)

if __name__ =='__main__':
	startTime = datetime.now()
	files, dirs, path = loadData(DIR_NAME, PATTERN)
	q = reconstructFolderStruct(dirs)
	
	# extractor(files[0]) #Only one file, use for testing.

	for f in files:
		extractor(f)

	#large dump may take a while
	json.dump(q, open('scripties.json', 'w+'))
	logging.info("Time it took to parse all files {}".format(datetime.now() - startTime))