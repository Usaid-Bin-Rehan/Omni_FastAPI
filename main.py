from fastapi import FastAPI
from Extensions.config_di import register_services
from Extensions.config_app import configure_app
from Extensions.config_endpoints import map_endpoints

def create_app() -> FastAPI:
    app = FastAPI()
    register_services(app)
    configure_app(app)
    map_endpoints(app)
    return app

app = create_app()

@app.get("/ping")
def ping():
    return {"ping": "pong - the app is running"}