
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh import index
import os, os.path,sys
from whoosh import index
from whoosh import qparser
from whoosh.qparser import QueryParser
import configparser


def index_search(dirname, search_fields, search_query):
    ix = index.open_dir(dirname)
    schema = ix.schema
    
    og = qparser.OrGroup.factory(0.9)
    mp = qparser.MultifieldParser(search_fields, schema, group = og)
    
    q = mp.parse(search_query)
    
    with ix.searcher() as s:
        results = s.search(q, terms=True, limit = 10)
        print("Search Results: ")
        # print(results[0:10])
        docwithpath=results[0]['path']
        textcontent=results[0]['textdata']
        print(docwithpath, "\n", textcontent)

# myQuery = str(sys.argv[1])
results_dict = index_search("indexdir", ['title','content'], "President")
