from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.predictor import predict_mole
from app.api.schemas.mole import MolePredictionResponse

router = APIRouter()

@router.post("/analyze", response_model=MolePredictionResponse)
async def analyze_mole(image: UploadFile = File(...)):
    try:
        image_bytes = await image.read()
        print(f" Received image: {image.filename} ({len(image_bytes)} bytes)")
        prediction = predict_mole(image_bytes)
        return prediction
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
