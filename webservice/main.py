from fastapi import FastAPI

from nuvox_algorithm import NuvoxAlgorithm
from webservice.api import api_router

app = FastAPI()

app.include_router(api_router)

app.state.nuvox_algorithm = NuvoxAlgorithm()
