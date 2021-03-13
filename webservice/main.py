from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from nuvox_algorithm import NuvoxAlgorithm
from webservice.api import api_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:3000',
        'http://192.168.1.193:3000',
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix='/api')

app.state.nuvox_algorithm = NuvoxAlgorithm()
