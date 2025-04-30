import streamlit as st
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from PIL import Image

# Load the pre-trained model
@st.cache_resource
def load_model():
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

model, scaler = load_model()

def preprocess_image(image):
    # Convert the image to grayscale
    image = image.convert("L")
    # Resize the image to 64x64 pixels
    image = image.resize((64, 64))
    # Convert the image to a numpy array
    image_array = np.array(image)
    # Flatten the array and reshapr it
    image_array = image_array.flatten().reshape(1, -1)
    return image_array

st.title('Smile Detection App')

# File uploader for image input
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_container_width=True)
    
    # Preprocess the image
    processed_image = preprocess_image(image)
    # Get probabilities of the image is smiling or not
    prediction_proba = model.predict_proba(processed_image)[0][1] 
    prediction = model.predict(processed_image)
    
    # Display the prediction
    smile_score =  int(prediction_proba * 100)
    st.slider("Smile Score", min_value=0, max_value=100, value=smile_score, disabled=True)

    if prediction[0] == 1:
        st.success("The person is smiling: " + str(smile_score) + "%")
    else:
        st.error("The person is not smiling: " + str(smile_score) + "%")