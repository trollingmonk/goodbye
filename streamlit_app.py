import streamlit as st
import numpy as np
from PIL import Image
import cv2
from pymongo import MongoClient


"""
def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def pencilsketch(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return(final_img)


st.title("Smile at camera 📷")
st.write("This is your chance to say Goodbye to Rahul Pawar and Wish him Best of Luck")

# collecting the input image from user camera 

file_image = st.camera_input(label = "Take a pic of you to be sketched out",label_visibility="hidden")

if file_image:
    input_img = Image.open(file_image)
    final_sketch = pencilsketch(np.array(input_img))
    one, two = st.columns(2)
    with one:
        st.write("**Input Photo**")
        st.image(input_img, use_column_width=True)
    with two:
        st.write("**Output Pencil Sketch**")
        st.image(final_sketch, use_column_width=True)
    im_pil = Image.fromarray(final_sketch)
    im_pil.save("final_image.jpeg")
    with open("final_image.jpeg", "rb") as file:
        st.download_button(
            label="Download",
            data=file,
            file_name="final_image.jpeg",
            mime="image/png")
    

  
#else:
#     st.write("Oooh something wrong with your Camera")
"""

ATLAS_URI = "mongodb+srv://sicaga9567:Pohapoha123@cluster0.nb0qv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

class AtlasClient ():
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

DB_NAME = 'sample_mflix'
COLLECTION_NAME = 'embedded_movies'
atlas_client = AtlasClient (ATLAS_URI, DB_NAME)
atlas_client.ping()
print ('Connected to Atlas instance! We are good to go!')
