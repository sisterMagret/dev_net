from fastapi import FastAPI


app: FastAPI = FastAPI()

app.get("/")
def retrieve():
    return {"message": "hello world"}