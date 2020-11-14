from fastapi import FastAPI,Request
import uvicorn
import json

app = FastAPI()


@app.get("/")
def index():
    return "Hii guyz"


@app.post("/github")
def api_github_response(request:Request):
    print(request.json())

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)