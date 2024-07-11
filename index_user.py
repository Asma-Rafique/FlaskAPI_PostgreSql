from fastapi import FastAPI
# # from DB.template import engine
from routes_.user import user
app = FastAPI()
app.include_router(user)
