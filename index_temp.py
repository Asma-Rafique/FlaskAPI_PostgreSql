from fastapi import FastAPI
# # from DB.template import engine
from routes_.endpoints import appp
# # from models.template import Base
# # from typing import Annotated
# # Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(appp)
# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


# @app.on_event("startup")
# async def on_startup():
#     await init_db()

# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run(app, host="0.0.0.0", port=8000)
