import os
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
import sys
import time
 
def createSearchableData(root):
    start_time = time.time()
    '''
    Schema definition: title(name of file), path(as ID), content(indexed
    but not stored),textdata (stored text content)
    '''
    schema = Schema(title=TEXT(stored=True),path=ID(stored=True),\
              content=TEXT,textdata=TEXT(stored=True))
    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")
 
    # Creating a index writer to add document as per schema
    ix = create_in("indexdir",schema)
    writer = ix.writer()
 
    filepaths = [os.path.join(root,i) for i in os.listdir(root)]
    for path in filepaths:
        fp = open(path,'r')
        print("Indexing file: ",path)
        text = fp.read()
        writer.add_document(title=path.split("/")[0], path=path,\
          content=text,textdata=text)
        fp.close()
    writer.commit()
    print("Time taken is ",time.time()-start_time)
 
root = "sampleCorpus"
createSearchableData(root)
