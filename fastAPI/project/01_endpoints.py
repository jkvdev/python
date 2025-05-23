from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world! I'm testing my FastAPI."}

@app.get("/about")
def get_about():
    return {
        "description": "This is a test API for learning FastAPI. Welcome to the About Page!"
    }


