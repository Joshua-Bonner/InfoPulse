import logging
import os

from dotenv import load_dotenv
from elasticsearch import Elasticsearch as ES

load_dotenv()

logger = logging.getLogger("uvicorn.error")

ES_HOST = os.getenv("ES_HOST")
ES_USERNAME = os.getenv("ES_USERNAME")
ES_PW = os.getenv("ES_PW")
ES_API_KEY = os.getenv("ES_API_KEY")
ES_API_KEY_JSON = os.getenv("ES_API_KEY_JSON")


class ESClient:
    def __init__(self):
        self.es = self._get_es_client()

    def _get_es_client(self):
        return ES(ES_HOST, api_key=ES_API_KEY, verify_certs=False)

    def search(self, index, query):
        return self.es.search(index=index, body=query)

    def insert_doc(self, index, id, doc):
        return self.es.index(index=index, id=id, body=doc)

    def get_doc(self, index, id):
        return self.es.get(index=index, id=id)

    def update_doc(self, index, id, doc):
        return self.es.update(index=index, id=id, body={"doc": doc})

    def delete_doc(self, index, id):
        return self.es.delete(index=index, id=id)
