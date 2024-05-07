from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
from fastapi.middleware.cors import CORSMiddleware
# Initialize FastAPI app
app = FastAPI(debug=True)

# Enable CORS
origins = [
    "http://localhost",
    "http://localhost:5173",  # Example front-end URL
    # Add more origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Load the Keras model
model = load_model('modelBiLstm.keras')

# Map class indices to class names
class_indices = {0: 'Mild_Demented', 1: 'Moderate_Demented', 2: 'Non_Demented', 3: 'Very_Mild_Demented'}

# Function to preprocess the image
def preprocess_image(img):
    # Convert image to RGB format if it has 4 channels (RGBA)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    # Preprocess the image as per your model's requirements (resize, normalize, etc.)
    # Example:
    img = img.resize((150, 150))
    img_array = np.array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array


# Define endpoint to receive image and return prediction
@app.post("/predict/")
async def predict_alzheimar(file: UploadFile = File(...)):
    try:
        # Read image file
        contents = await file.read()
        # Convert image file to image object
        img = Image.open(io.BytesIO(contents))
        # Preprocess the image
        processed_img = preprocess_image(img)
        # Make prediction
        prediction = model.predict(processed_img)
        # Get predicted class index
        predicted_class_index = np.argmax(prediction)
        # Get predicted class name
        predicted_class_name = class_indices[predicted_class_index]
        # Send response with predicted class
        return JSONResponse( predicted_class_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

