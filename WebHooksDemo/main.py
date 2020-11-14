from fastapi import FastAPI,Request
import uvicorn
import json

app = FastAPI()


@app.get("/")
def index():
    return "Hii guyz"


@app.post("/github")
async def api_github_response(request:Request):
    data = json.loads(request.payload)
    print(data)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)