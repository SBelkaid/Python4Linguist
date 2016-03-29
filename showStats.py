import json
from collections import defaultdict
import numpy as np
from collections import Counter
from datetime import datetime
from parser import freq


def returnTotal(data):
	"""
	looping throuh the scripties dictionairy and appending values. If values are lists
	they are extended to return the total per language and programme.
	"""
	totals = {}
	for programme in data.keys():
		totals[programme] = {}
		for language in data[programme]:
			totals[programme][language] = defaultdict(list)
			for author in data[programme][language]:
				author_content = data[programme][language].get(author)
				totals[programme][language]['all_sentences'].append(author_content['amount_of_sentences'])
				totals[programme][language]['all_tokens'].append(author_content['Amount_of_words'])
				totals[programme][language]['all_tokens'].append(author_content['amount_of_other_tokens'])
				totals[programme][language]['raw_all_tokens'].extend(author_content['all_other_tokens'])
				totals[programme][language]['raw_all_tokens'].extend(author_content['all_words'])
				totals[programme][language]['all_types'].append(author_content['amount_of_types'])
				totals[programme][language]['raw_all_types'].extend(author_content['all_types'])
				totals[programme][language]['all_people'].extend(author_content['all_people'])
				totals[programme][language]['all_entities'].extend(author_content['all_entities'])
				totals[programme][language]['all_locations'].extend(author_content['all_dbp_urls_all_places'])
				totals[programme][language]['10_longest_sentences'].extend(author_content['10_longest_sentences'])
	return totals

def statsPerLanguageAndProgram(data, n=5):
	'''
	This function calculates the following stats per language and programme:
	average amount of sentences
	average amount of tokens
	average amount of types
	type token ratio
	most frequent people
	most frequent locations
	frequency of each entity
	'''

	for programme in data.keys():
		for language in data[programme]:
			print '\n\n\n\n', programme, language
			print '\tAverage amount of sentences', np.mean(map(int,data[programme][language]['all_sentences']))
			print '\tAverage amount of tokens', np.mean(data[programme][language]['all_tokens'])
			print '\tAverage amount of types', np.mean(data[programme][language]['all_types'])
			print '\tType/token ratio per language ratio ', \
					(np.mean(data[programme][language]['all_types'])/np.mean(data[programme][language]['all_tokens']))
			print '\tMost frequent locations', Counter(data[programme][language]['all_locations']).most_common(n)
			print '\tMost frequent people', Counter(data[programme][language]['all_people']).most_common(n)
			print '\tFrequency entities', Counter(data[programme][language]['all_entities']).items()


def statsPerProgramme(programme_totals, n=5):
	'''
	This function calculates the following stats per programme:
	average amount of sentences
	average amount of tokens
	average amount of types
	type token ratio
	most frequent people
	most frequent locations
	frequency of each entity
	'''
	for programme in programme_totals:
		all_sentences_course = []
		all_tokens_course = []
		all_types_course = []
		all_people_course = []
		all_locations_course = []
		all_entities_course = []
		all_longest_sentences_course = []
		all_raw_types_course = []
		all_raw_tokens_course = []
		for language in programme_totals[programme]:
			all_sentences_course.extend(programme_totals[programme][language]['all_sentences'])
			all_tokens_course.extend(programme_totals[programme][language]['all_tokens'])
			all_types_course.extend(programme_totals[programme][language]['all_types'])
			all_people_course.extend(programme_totals[programme][language]['all_people'])
			all_locations_course.extend(programme_totals[programme][language]['all_locations'])
			all_entities_course.extend(programme_totals[programme][language]['all_entities'])
			all_longest_sentences_course.extend(map(tuple,programme_totals[programme][language]['10_longest_sentences']))
			all_raw_types_course.extend(programme_totals[programme][language]['raw_all_types'])
			all_raw_tokens_course.extend(programme_totals[programme][language]['raw_all_tokens'])
		print 'Average amount of sentences in', programme, np.mean(map(int, all_sentences_course))
		print 'Average amount of tokens in', programme, np.mean(all_tokens_course)
		print 'Average amount of types in', programme, np.mean(all_types_course)
		print 'Type/token ration', programme, np.mean(all_types_course)/np.mean(all_tokens_course)
		print 'Most frequent locations in', programme, Counter(all_locations_course).most_common(n)
		print 'Most frequent people in', programme, Counter(all_people_course).most_common(n)
		print 'Frequency entities', Counter(all_entities_course)
		print 'Frequency each type', Counter(all_raw_types_course)
		print 'Frequency each token', Counter(all_raw_tokens_course)
		print '\n\n\n\n'


if __name__=='__main__':
	print "Loading data"
	startTime = datetime.now()
	scripties = json.load(open('scripties.json', 'r'))
	print "Loading took: {}".format(datetime.now() - startTime)
	stats = returnTotal(scripties)
	# statsPerLanguageAndProgram(stats)
	statsPerProgramme(stats)



		

