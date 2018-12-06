import json
import requests
import pprint
def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. The grader will supply the URL as an argument to
    # the function; you do not need to construct the address or call this
    # function in your grader submission.
    # 
    # Once you've done this, return the name of the number 1 top artist in
    # Spain.

    '''
    Application name 	udacity
    API key 	*
    Shared secret 	*
    Registered to 	*
    http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=YOUR_API_KEY&format=json
    '''
    
    #return ... # return the top artist in Spain

api_key='*'
url='http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key='+api_key+'&limit=2&format=json'
data=requests.get(url).text # hacer get url
data=json.loads(data)
pp=pprint.PrettyPrinter(indent=2)
pp.pprint(data)
print data['topartists']['artist'][0]['name']
