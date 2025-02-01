import asyncio
from fastapi import FastAPI

application = FastAPI()


@application.get("/greeting")
async def greeting():
    await asyncio.sleep(20)
    return {"message": "Hello World Mandeep"}


@application.get("/greeting2")
async def greeting2():
    await asyncio.sleep(5)
    return {"message": "Hello Python from method 2"}


@application.post("/submit")
def submit(data:dict):
    return {"message":"Data submitted successfully!","data":data["name"]}