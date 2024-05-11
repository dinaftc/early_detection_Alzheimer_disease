from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.preprocessing import image
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
class_indices = {0: 'Mild_Demented_augmented', 1: 'Moderate_Demented_augmented', 2: 'Non_Demented', 3: 'Very_Mild_Demented'}




# Define endpoint to receive image and return prediction
@app.post("/predict/")
async def predict_alzheimar(file: UploadFile = File(...)):
    try:
        # Read image file
        contents = await file.read()
        # Convert image file to image object
        
        img = image.load_img(io.BytesIO(contents), target_size=(150, 150))  # Assuming input size of your model is (150, 150)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array /= 255.0  # Normalize pixel values

        # Predict the class probabilities
        prediction = model.predict(img_array)

        # Get the predicted class label
        predicted_class_index = np.argmax(prediction)
        predicted_class_name = class_indices[predicted_class_index]
        # Send response with predicted class
        return JSONResponse( predicted_class_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
