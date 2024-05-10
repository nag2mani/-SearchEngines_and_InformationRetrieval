
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh import index
import os, os.path,sys
from whoosh import index
from whoosh import qparser
from whoosh.qparser import QueryParser
import configparser


def index_search(dirname, search_fields, search_query, numResults):
    ix = index.open_dir(dirname)
    schema = ix.schema
    numOutput = int(numResults)

    og = qparser.OrGroup.factory(0.9)
    mp = qparser.MultifieldParser(search_fields, schema, group = og)
    
    q = mp.parse(search_query)
    
    i=0
    with ix.searcher() as s:
        results = s.search(q, terms=True, limit = 10)
        print("Search Results: ")

        for i in range(numOutput):
            docwithpath=results[i]['path']
            textcontent=results[i]['textdata']
            print(docwithpath, "\n", textcontent)
            # print("Doc Name: ",docwithpath[docwithpath.rindex('/'+1):])


config = configparser.RawConfigParser()
config.read("config.properties")

myQuery = config.get('var','myQuery')
indexdir = config.get('var','indexdir')
numResults = config.get('var','numResults')


# myQuery = str(sys.argv[1])
results_dict = index_search(indexdir, ['title','content'], myQuery, numResults)

