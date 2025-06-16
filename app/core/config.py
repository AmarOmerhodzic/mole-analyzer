from pydantic import BaseSettings

class Settings(BaseSettings):
    MODEL_PATH: str = "models/skin_cancer_model.h5"

    class Config:
        env_file = ".env"

settings = Settings()
