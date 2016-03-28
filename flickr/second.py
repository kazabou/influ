import json
import urllib2

import flickr_api
from flickr_api.api import flickr


key = "aa002510472d4cf5eb72710428014d3b"
secret = "22829bcbe03a185a"

flickr_api.set_keys(key,secret)

print flickr_api.License


# url = "https://api.flickr.com/services/rest/?method=flickr.contacts.getPublicList&api_key=a56792147838e34f805008fc0d2ff4fd&user_id=21729155%40N00&format=json&nojsoncallback=1&auth_token=72157665946659450-23cf53c8e42e55e1&api_sig=d10ab6395409030d4d64e88bc3ef2ef2"
url = "https://api.flickr.com/services/rest/?method=flickr.contacts.getPublicList&api_key=aa002510472d4cf5eb72710428014d3b&user_id=21729155%40N00&format=json&nojsoncallback=1&api_secret=22829bcbe03a185a"



# contacts = urllib2.urlopen(url).read()
#
# dic = json.loads(contacts)
#
# for contact in dic['contacts']['contact']:
#     print contact['nsid']





def getContacts(userId, key, secret):

    url = "https://api.flickr.com/services/rest/?method=flickr.contacts.getPublicList&api_key="+key+"&user_id="+userId+"&format=json&nojsoncallback=1&api_secret="+secret
    contacts = urllib2.urlopen(url).read()

    dic = json.loads(contacts)

    for contact in dic['contacts']['contact']:
        print contact['nsid']




userId =  "50979393@N00"
getContacts(userId,key, secret)
