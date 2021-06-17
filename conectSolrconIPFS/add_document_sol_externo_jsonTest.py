#http://buele.github.io/python/2015/11/07/python-solr-add-document.html
import http.client
import json
import sys


#connection = http.client.HTTPConnection("localhost",8983)


connection = http.client.HTTPConnection("localhost",8983)

headers = {'Content-type': 'application/json'}

#foo = {'add': {'doc': {'id': "leid", 'compName_s': "compo"}, 'boost': 1, 'overwrite': False, 'commitWithin': 1000}}


# read file
with open('jsonTest.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)


#json_foo = json.dumps(foo)

foo1 = {'add': {'doc': obj, 'boost': 1, 'overwrite': False, 'commitWithin': 1000}}
json_foo1 = json.dumps(foo1)


#print(obj)
#print(json_foo )
#print(json_foo1 )


connection.request('POST', '/solr/demo/update?wt=json', json_foo1, headers)

response = connection.getresponse()
print(response.read().decode())

#run script
#python3 add_document.py "test_id" "Test Title!"

#output
#{"responseHeader":{"status":0,"QTime":8}}

