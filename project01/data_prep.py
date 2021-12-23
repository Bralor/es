import json

from elasticsearch import Elasticsearch

# filenames
index_name: str = "gastronomical"
doc_type: str = "recipes"

# instantiate a new client instance
client = Elasticsearch("http://localhost:9200")

# call an API 
response = client.info()

