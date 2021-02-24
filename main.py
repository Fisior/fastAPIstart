import random
from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id")
def read_item(item_id: int, q: Optional[str] = None):
    return {"itemd_id": item_id, "q": q}


@app.get("/rand")
async def rand():
    return random.randint(0, 100)
  