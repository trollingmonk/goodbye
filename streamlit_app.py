import streamlit as st
from PIL import Image
from pymongo import MongoClient
import io
from multiprocessing.pool import ThreadPool


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

st.header("Say Goodbye to Rahul with a Picture 📸", divider=True)

file_image = st.camera_input("Capture an image",label_visibility="hidden")
if file_image:
    image = Image.open(file_image)
    st.image(image, caption='It is You ✌️', use_container_width=True)
    one, two, three = st.columns(3)
    one.button(":sparkles:", use_container_width=True,disabled=True)
    three.button(":star2:", use_container_width=True,disabled=True)
    # Button to save image
    if two.button("Save your Photographic Greet"):
        atlas_uri=st.secrets["database_uri"]
        db_name=st.secrets["db_name"]
        COLLECTION_NAME=st.secrets["collection_name"]
        atlas_client=AtlasClient(atlas_uri,db_name)
        images=atlas_client.get_collection(collection_name=COLLECTION_NAME)
        im=Image.open(file_image)
        image_bytes=io.BytesIO()
        im.save(image_bytes, format='JPEG')
        image={'data': image_bytes.getvalue()}
        image_id=images.insert_one(image).inserted_id
        st.success("Your Greeting has been saved in Memory Ledger 📓!")
		
# Function to retrieve images
def get_images():
    atlas_uri=st.secrets["database_uri"]
    db_name='imagedb'
    COLLECTION_NAME='images'
    atlas_client=AtlasClient(atlas_uri,db_name)
    images=atlas_client.find(collection_name=COLLECTION_NAME)
    return [image['data'] for image in images]

st.header(" ", divider=True)
left, middle, right = st.columns(3)
left.button(":maple_leaf:", use_container_width=True,disabled=True)
right.button(":fallen_leaf:", use_container_width=True,disabled=True)
if middle.button("View All Greets 🎥",use_container_width=True):
    pool = ThreadPool(processes=1)
    thread = pool.apply_async(get_images)
    images_data = thread.get()
    cols = st.columns(4)
    for i in range(len(images_data)):
        for j in range(4):
            index = i * 4 + j
            if index < len(images_data):
                cols[j].image(images_data[index])
    st.balloons()
st.header(" ", divider=True)
