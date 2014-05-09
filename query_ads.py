import math
import json
import urllib2
import pickle
import time
import numpy as np

def query_ads_get_hits(url):
	print url
	time.sleep(1)
	response = urllib2.urlopen(url)
	metrics = json.load(response)
#	print metrics.keys() # for reference
	hits = metrics['meta']['hits']
	return hits


# need ADS API key (stored as only text file 
# called secret.py)
from secret import my_key

# get years for AAS Meetings
lookup_years = []
lookup_meetings = []
for i in range(182,186):
	# print i,1993 + math.floor((i-180)/2.)
	lookup_years.append(1993 + math.floor((i-181)/2.))
	lookup_meetings.append(i)
	
# check sizes agree...

# aas meetings and sessions from save file
AAS_num, AAS_session_num, AAS_session_title=pickle.load(open('AAS_Lists.pickle'))

for i in range(0,len(AAS_num)):
	
	#### QUERY SET UP ####
	
	# base url
	stem = 'http://adslabs.org/adsabs/api/search/metrics/?q='
	
	# search parameters
	aas = AAS_num[i]
	year = lookup_years[lookup_meetings.index(int(aas))]
	session = AAS_session_num[i]
	strsess = '%02d' % int(session)
	strsess
	print aas, year, session
	if int(aas) == 182:
		search = 'bibcode:"'+str(int(year))+'AAS...'+str(int(aas))+'.'+strsess+'*"'
	else:
		search = 'bibcode:"'+str(int(year))+'AAS...'+str(int(aas))+strsess+'*"'
	
	# shouldn't be necessary, but add filters for safety
	filter = 'filter=database:astronomy+property:not_refereed'
	# output only includes titles
	# API can only show 200 entries
	show = 'fl=title'
	
	# the developer API key
	key = 'dev_key='+my_key
	url = stem+search+'&'+filter+'&'+show+'&'+key
	
	print url
	
	hits = query_ads_get_hits(url)
	print hits

# this is what a single query looks like (without the dev_key)
# 
#http://adslabs.org/adsabs/api/search/?q=bibcode:"1993AAS...182*"&filter=database:astronomy+property:not_refereed&fl=title&dev_key=oqRuiHkV89PToMsg
#http://adslabs.org/adsabs/api/search/?q=bibcode:"2013AAS...*"&fl=title&filter=database:astronomy+property:not_refereed
