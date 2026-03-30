from fastapi import FastAPI
from app.routers import post

app = FastAPI() 

app.include_router(post.router)