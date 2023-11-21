# main.py
from fastapi import FastAPI
from fastapi.routing import APIRouter

import uvicorn

router = APIRouter(prefix="/api")


@router.get("/hello-world")
async def root():
    return {"message": "Hello World"}


app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
