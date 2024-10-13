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

st.title("Smile at camera 📷")
st.write("This is your chance to say Goodbye to Rahul Pawar and Wish him Best of Luck")

with st.container():
    file_image = st.camera_input(label = "Take a pic of you to be sketched out",label_visibility="hidden")
    if file_image:
        atlas_uri="mongodb+srv://sicaga9567:pohapoha123@cluster0.nb0qv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        db_name='imagedb'
        COLLECTION_NAME='images'
        atlas_client=AtlasClient(atlas_uri,db_name)
        images=atlas_client.get_collection(collection_name=COLLECTION_NAME)
        im=Image.open(file_image)
        image_bytes=io.BytesIO()
        im.save(image_bytes, format='JPEG')
        image={'data': image_bytes.getvalue()}
        image_id=images.insert_one(image).inserted_id

with st.container():
    atlas_uri="mongodb+srv://sicaga9567:pohapoha123@cluster0.nb0qv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    db_name='imagedb'
    COLLECTION_NAME='images'
    atlas_client=AtlasClient(atlas_uri,db_name)
    images=atlas_client.get_collection(collection_name=COLLECTION_NAME)
    result = list(images.find())
    st.write(result)
        

