# -*- coding: UTF-8 -*-
#!/usr/bin/env python2

from ATLASAPI import *
import json

def loadJSONfile(f):
    with open(f) as json_data:
        d = json.load(json_data)
    return d;

newPropertyName = "myCustomProperty"
atlasTypeName = "hive_table"


jsonStr = loadJSONfile("Data/update_hive_table_type.json")
print jsonStr

hiveColResult = atlasPUT("/api/atlas/types", jsonStr)
print json.dumps(hiveColResult, indent=4, sort_keys=True)