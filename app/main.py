import uvicorn
from app.database.database import async_get_db
from fastapi import FastAPI
from app.routers import tweets, users

session = async_get_db()


app = FastAPI(debug=True)


app.include_router(users.router)
app.include_router(tweets.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
