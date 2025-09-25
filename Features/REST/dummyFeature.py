from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def say_hello():
    return {"message": "Hello from DummyFeature"}

@router.get("/ping")
def ping():
    return {"message": "pong"}
