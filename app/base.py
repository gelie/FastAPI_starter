from fastapi import FastAPI

app = FastAPI(title="FastAPI Starter App")


@app.get("/")
def home():
    return {"message": "Hello World!!"}
