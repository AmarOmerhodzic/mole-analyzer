from fastapi import FastAPI
from app.api.endpoints.mole import router as mole_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only, restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include the mole analysis endpoint
app.include_router(mole_router, prefix="/api/endpoints/mole", tags=["mole"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Mole Analyzer API!"}
