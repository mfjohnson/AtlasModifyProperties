import requests
import json
import sys


ATLAS_DOMAIN="server1"
ATLAS_PORT="21000"

RANGER_DOMAIN="server1.hdp"
RANGER_PORT="6080"

def atlasGET( restAPI ) :
## TODO Verify received code = 200 or else produce an error
    url = "http://"+ATLAS_DOMAIN+":"+ATLAS_PORT+restAPI
    r= requests.get(url, auth=("admin", "admin"))
    return(json.loads(r.text));


def atlasPOST( restAPI, data) :
    url = "http://" + ATLAS_DOMAIN + ":" + ATLAS_PORT + restAPI
    print (url)
    r = requests.post(url, auth=("admin", "admin"),json=data)
    return (json.loads(r.text));


def atlasPUT( restAPI, data) :
    url = "http://" + ATLAS_DOMAIN + ":" + ATLAS_PORT + restAPI
    print "URL request = curl  -ivH -u admin:admin -d \"@update_hive_table_type.json\" --header \"Content-Type: application/json\" -X PUT %s" % (url)
    r = requests.put(url, auth=("admin", "admin"),json=data)

    return (json.loads(r.text));


