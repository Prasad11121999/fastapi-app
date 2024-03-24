from fastapi import FastAPI

app= FastAPI()

@app.get("/")
async def read_root():
    return {"message":"Hellow! world"}

@app.get("/items/{item_id}")
async def read_item(item_id: int,Name:str=None):
    return {"item_id": item_id, "Name": Name}