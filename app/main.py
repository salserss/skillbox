import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.routers import media, tweets, users

app: FastAPI = FastAPI(title="main")
app_api: FastAPI = FastAPI(title="api")

app.mount("/api", app_api, name='api')
app.mount("/", StaticFiles(directory="static", html=True), name="static")

templates = Jinja2Templates(directory="static")

origins = ["http://127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


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


app_api.include_router(media.router)
app_api.include_router(tweets.router)
app_api.include_router(users.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
