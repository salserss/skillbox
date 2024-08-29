import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app_api = FastAPI()

app.mount("/api", app_api)
app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return HTMLResponse("index.html")


@app_api.get("/users/me")
async def get_user_me():
    return {
        "result": "true",
        "user": {
            "id": 1,
            "name": "str",
            "followers": [],
            "following": []
        }
    }


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
