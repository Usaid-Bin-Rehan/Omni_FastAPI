from fastapi import FastAPI
from Features.REST.dummyFeature import router

def configure_app(app: FastAPI):
    app.include_router(router)
    print("[INFO] App configured")
