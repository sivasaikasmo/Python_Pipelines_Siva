import json
import pandas as pd
def extract_json(collection):
    documents=collection.find({})
    d=list(documents)
    for doc in d:
        doc.pop('_id', None)
    return d
