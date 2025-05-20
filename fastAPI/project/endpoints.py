# import fastapi 

from fastapi import FastAPI

# create API object
app = FastAPI()

# Get first endpoint/ route
# /hello    /get-item
@app.get("/")
# Function that would be called when the endpoint is hit
# it doesn't matter the name of the function as long as it's
# right under it gets called
def read_root():
    return {"Hello": "World, I'm testing my FastAPI"}
  
@app.get('/about')
def about():
    return {"Description": "This is a test API for learning FastAPI. Welcome to the About Page!"}

