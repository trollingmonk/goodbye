import streamlit as st
import numpy as np
from PIL import Image
import cv2
from pymongo import MongoClient

class AtlasClient():
   def __init__ (self, altas_uri, dbname):
       self.mongodb_client = MongoClient(altas_uri)
       self.database = self.mongodb_client[dbname]
   ## A quick way to test if we can connect to Atlas instance
   def ping (self):
       self.mongodb_client.admin.command('ping')
   def get_collection (self, collection_name):
       collection = self.database[collection_name]
       return collection
   def find (self, collection_name, filter = {}, limit=0):
       collection = self.database[collection_name]
       items = list(collection.find(filter=filter, limit=limit))
       return items

ATLAS_URI="mongodb+srv://sicaga9567:pohapoha123@cluster0.nb0qv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME='sample_mflix'
COLLECTION_NAME='embedded_movies'
atlas_client=AtlasClient(ATLAS_URI, DB_NAME)
atlas_client.ping()
st.write('Connected to Atlas instance! We are good to go!')
movies=atlas_client.find(collection_name=COLLECTION_NAME,limit=15)
while len(movies):
   st.write(movies[0]["title"])
