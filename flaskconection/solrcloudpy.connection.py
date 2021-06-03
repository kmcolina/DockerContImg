from solrcloudpy.connection import SolrConnection


conn = SolrConnection(server=["localhost:8983","localhost:8983"], version="6.0.0")

print(conn)
z=conn["demo"].search({'q':'*:*'}).result

print(z)

