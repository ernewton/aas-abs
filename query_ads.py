import json
import urllib2
from secret import my_key

stem = 'http://adslabs.org/adsabs/api/search/metrics/?q='
year = '1993'
aas = '183'
session = ''
search = 'bibcode:"'+year+'AAS...'+session+'*"'
filter = 'filter=database:astronomy+property:not_refereed'
show = 'fl=title'
key = 'dev_key='+my_key

url = stem+search+'&'+filter+'&'+show+'&'+key

response = urllib2.urlopen(url)
metrics = json.load(response)
print metrics.keys() # for reference
metrics['meta']['hits']

# http://adslabs.org/adsabs/api/search/?q=bibcode:"2013AAS...*"&fl=title&filter=database:astronomy+property:not_refereed
