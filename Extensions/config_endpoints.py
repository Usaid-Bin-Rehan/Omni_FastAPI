from fastapi import FastAPI
from Features.REST import dummyFeature #, countryFeature

def map_endpoints(app: FastAPI):
    app.include_router(dummyFeature.router, prefix="/dummy", tags=["DummyFeature"])
#    app.include_router(countryFeature.router, prefix="/country", tags=["CountryFeature"])
