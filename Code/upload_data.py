import pandas as pd
import wget
import os
from pymongo import MongoClient

connection = 'mongodb://'+str(os.sys.argv[1])+':27017/'
url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide.xlsx'

client = MongoClient(connection)
database = client['covid']
collection = database['Worldwide']


def excel_to_json():
    filename = wget.download(url)
    data = pd.read_excel(filename)
    os.remove(filename)
    return data.to_dict('records')


collection.delete_many({})
collection.insert_many(excel_to_json())
