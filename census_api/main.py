## Import API census
from census import Census
## Import library to decode FIPS to places
from us import states

## Paste your api key in the line bellow
api_key = "PASTE YOUR API KEY HERE"
 
c = Census(api_key)
c.acs5.get(('NAME', 'B25034_010E'),
          {'for': 'state:{}'.format(states.MD.fips)})

## 36 = New York
print (states.lookup('36').abbr)
print(c.acs5.tables())
