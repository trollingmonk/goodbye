import streamlit as st
from PIL import Image
from pymongo import MongoClient
import io


class AtlasClient():
   def __init__ (self, altas_uri, dbname):
       self.mongodb_client = MongoClient(altas_uri)
       self.database = self.mongodb_client[dbname]
   def ping(self):
       self.mongodb_client.admin.command('ping')
   def get_collection(self, collection_name):
       collection = self.database[collection_name]
       return collection
   def find(self, collection_name, filter = {}, limit=0):
       collection = self.database[collection_name]
       items = collection.find(filter=filter, limit=limit)
       return items

atlas_uri="mongodb+srv://sicaga9567:pohapoha123@cluster0.nb0qv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
db_name='imagedb'
COLLECTION_NAME='images'
atlas_client=AtlasClient(atlas_uri,db_name)
images=atlas_client.get_collection(collection_name=COLLECTION_NAME)
result = list(images.find())
st.write(result)

if 'count' not in st.session_state:
    st.session_state.count = 0

if 'quotes' not in st.session_state:
    st.session_state.quotes = result

def display_quote():
    quote = st.session_state.quotes[st.session_state.count]
    st.write(quote)

def next_quote():
    if st.session_state.count + 1 >= len(st.session_state.quotes):
        st.session_state.count = 0
    else:
        st.session_state.count += 1

def previous_quote():
    if st.session_state.count > 0:
        st.session_state.count -= 1

st.title("Inspirational Quotes")

display_quote()

col1, col2 = st.columns(2)

with col1:
    if st.button("⏮️ Previous", on_click=previous_quote):
        pass

with col2:
    if st.button("Next ⏭️", on_click=next_quote):
        pass
