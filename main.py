import os
import numpy as np
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model
from google.cloud import storage

def download_image_from_gcs(image_bucket_name, image_filename):
    # Initialize a client object for interacting with Cloud Storage
    storage_client = storage.Client()
    bucket = storage_client.bucket(image_bucket_name)
    
    # Download the image file to a local directory
    image_blob_name = 'images/' + image_filename  # Assuming images are stored in 'images' folder in the bucket
    image_local_path = '/tmp/' + image_filename  # Temporary directory for storing the image file
    blob = bucket.blob(image_blob_name)
    blob.download_to_filename(image_local_path)
    
    return image_local_path

def download_model_from_gcs(model_bucket_name, model_filename):
    # Initialize a client object for interacting with Cloud Storage
    storage_client = storage.Client()
    bucket = storage_client.bucket(model_bucket_name)
    
    # Download the model file to a local directory
    model_blob_name = 'models/' + model_filename  # Assuming models are stored in 'models' folder in the bucket
    model_local_path = '/tmp/' + model_filename  # Temporary directory for storing the model file
    blob = bucket.blob(model_blob_name)
    blob.download_to_filename(model_local_path)
    
    return model_local_path

def getPrediction(image_bucket_name, image_filename, model_bucket_name, model_filename):
    classes = ['Actinic keratoses', 'Basal cell carcinoma', 
               'Benign keratosis-like lesions', 'Dermatofibroma', 'Melanoma', 
               'Melanocytic nevi', 'Vascular lesions']
    
    le = LabelEncoder()
    le.fit(classes)
    le.inverse_transform([2])
    
    # Download the image file from Google Cloud Storage
    image_path = download_image_from_gcs(image_bucket_name, image_filename)
    
    # Load the image
    img = np.asarray(Image.open(image_path).resize((SIZE, SIZE)))
    img = img / 255.  # Scale pixel values
    img = np.expand_dims(img, axis=0)  # Get it ready as input to the network
    
    # Download the model file from Google Cloud Storage
    model_path = download_model_from_gcs(model_bucket_name, model_filename)
    
    # Load the model
    my_model = load_model(model_path)
    
    pred = my_model.predict(img)  # Predict
    
    # Convert prediction to class name
    pred_class = le.inverse_transform([np.argmax(pred)])[0]
    print("Diagnosis is:", pred_class)
    return pred_class

# test_prediction = getPrediction('your_image_bucket_name', 'download.jfif', 'your_model_bucket_name', 'model.h5')
