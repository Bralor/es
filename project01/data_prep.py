from elasticsearch import Elasticsearch

# instantiate a new client instance
client = Elasticsearch("http://localhost:9200")

# call an API 
response = client.info()

