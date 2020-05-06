import pandas as pd
import wget
import os
from pymongo import MongoClient

url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide.xlsx'


def excel_to_json():
    filename = wget.download(url)
    data = pd.read_excel(filename)
    os.remove(filename)
    return data.to_dict('records')

def upload_data(uri):
    #connection = 'mongodb://'+ip+':27017/'
    client = MongoClient(uri)
    database = client['covid']
    collection = database['Worldwide']

    #collection.delete_many({})
    collection.insert_many(excel_to_json())


upload_data(os.argv[1])