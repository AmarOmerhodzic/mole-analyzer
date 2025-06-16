import numpy as np
from PIL import Image
import io
from app.models.model_loader import model
import tensorflow as tf

def predict_mole(image_bytes):

    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((180, 180), resample=Image.Resampling.LANCZOS)  
    
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.efficientnet.preprocess_input(image)  
    
    image = np.expand_dims(image, axis=0)
    
    malignant_prob = float(model.predict(image, verbose=0)[0][0])
    
    THRESHOLD = 0.25
    result = "malignant" if malignant_prob >= THRESHOLD else "benign"
    
    confidence = malignant_prob if result == "malignant" else (1 - malignant_prob)
    
    return {
        "result": result,
        "confidence": round(confidence * 100, 2),
    }
