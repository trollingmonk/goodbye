import streamlit as st
from PIL import Image
from pymongo import MongoClient
import io
import threading


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

file_image = st.camera_input("Capture an image",label_visibility="hidden")
if file_image:
    image = Image.open(file_image)
    st.image(image, caption='Captured Image', use_column_width=True)

        # Button to save image
    if st.button("Save your Greeting"):
        atlas_uri=st.secrets["database_uri"]
        db_name='imagedb'
        COLLECTION_NAME='images'
        atlas_client=AtlasClient(atlas_uri,db_name)
        images=atlas_client.get_collection(collection_name=COLLECTION_NAME)
        im=Image.open(file_image)
        image_bytes=io.BytesIO()
        im.save(image_bytes, format='JPEG')
        image={'data': image_bytes.getvalue()}
        image_id=images.insert_one(image).inserted_id
        st.success("Your Greeting has been Captured Successfully!")
		
# Function to retrieve images
def get_images():
    atlas_uri=st.secrets["database_uri"]
    db_name='imagedb'
    COLLECTION_NAME='images'
    atlas_client=AtlasClient(atlas_uri,db_name)
    images=atlas_client.find(collection_name=COLLECTION_NAME)
    return [image['data'] for image in images]

# Streamlit app
st.title("Greeting Gallery for Peoples who wished him ")

if st.button("Load Greets"):
    #images_data = threading.Thread(target=get_images)
    #images_data.start()
    #images_data.join()
    images_data = get_images()
    cols = st.columns(4)
    st.write(len(images_data))
    #for img in images_data:
    #    pil_img=Image.open(io.BytesIO(img['data']))
    #    cols[i % 4].image(pil_img, use_column_width=True)
    #cols = st.columns(4)
    for i in range(len(images_data)):
        for j in range(4):
            index = i * 4 + j
            if index < len(images_data):
                cols[j].image(images_data[index], caption=f"Image {index + 1}")

