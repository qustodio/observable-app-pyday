import logging
import os
import random
import time
import httpx
import uvicorn
from typing import Optional
from fastapi import FastAPI, Response

APP_NAME = os.environ.get("APP_NAME", "blueprints-app")

app = FastAPI()


@app.get("/api/blueprints")
async def read_root():
    logging.error("Hello World")
    return {"Message": "Ola k ase?"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    logging.error("items")
    return {"item_id": item_id, "q": q}


@app.get("/io_task")
async def io_task():
    time.sleep(1)
    logging.error("io task")
    return "IO bound task finish!"


@app.get("/cpu_task")
async def cpu_task():
    for i in range(1000):
        n = i * i * i
    logging.error("cpu task")
    return "CPU bound task finish!"


@app.get("/random_status")
async def random_status(response: Response):
    response.status_code = random.choice([200, 200, 300, 400, 500])
    logging.error("random status")
    return {"path": "/random_status"}


@app.get("/random_sleep")
async def random_sleep(response: Response):
    time.sleep(random.randint(0, 5))
    logging.error("random sleep")
    return {"path": "/random_sleep"}


@app.get("/error_test")
async def random_sleep(response: Response):
    logging.error("got error!!!!")
    raise ValueError("value error")


# @app.get("/chain")
# async def chain(response: Response):
#
#     headers = {}
#     inject(headers)  # inject trace info to header
#     logging.critical(headers)
#
#     async with httpx.AsyncClient() as client:
#         await client.get(f"http://localhost:8000/", headers=headers,)
#     async with httpx.AsyncClient() as client:
#         await client.get(f"http://{TARGET_ONE_HOST}:8000/io_task", headers=headers,)
#     async with httpx.AsyncClient() as client:
#         await client.get(f"http://{TARGET_TWO_HOST}:8000/cpu_task", headers=headers,)
#     logging.info("Chain Finished")
#     return {"path": "/chain"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
