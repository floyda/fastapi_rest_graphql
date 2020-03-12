"""
main.py
"""
from fastapi import FastAPI
from routers import locations, login

app = FastAPI()

app.include_router(login.router)
app.include_router(locations.router)

    