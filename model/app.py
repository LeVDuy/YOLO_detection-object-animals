from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI()

# Load model 
model = YOLO("model/my_model.pt")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        # Chạy inference
        results = model(image)

        # Trả kết quả dạng JSON
        return JSONResponse(content=results[0].to_json())

    except Exception as e:
        return JSONResponse(content={"error": str(e)})
