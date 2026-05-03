import os

class Config:
    APP_NAME = "Order Service"
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"