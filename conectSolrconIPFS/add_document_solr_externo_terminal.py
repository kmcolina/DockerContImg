#http://buele.github.io/python/2015/11/07/python-solr-add-document.html
import http.client
import json
import sys


#connection = http.client.HTTPConnection("localhost",8983)


connection = http.client.HTTPConnection("localhost",8983)

headers = {'Content-type': 'application/json'}

foo = {'add': {'doc': {'id': sys.argv[1], 'compName_s': sys.argv[2]}, 'boost': 1, 'overwrite': False, 'commitWithin': 1000}}
json_foo = json.dumps(foo)

connection.request('POST', '/solr/demo/update?wt=json', json_foo, headers)

response = connection.getresponse()
print(response.read().decode())

#run script
#python3 add_document.py "test_id" "Test Title!"

#output
#{"responseHeader":{"status":0,"QTime":8}}

