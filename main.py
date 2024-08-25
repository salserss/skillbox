from fastapi import FastAPI, Path

app: FastAPI = FastAPI()
app_api: FastAPI = FastAPI(title='Twitter Clone')
id_path = Path(..., title='Twitter Clone')

app.mount('/api', app_api)
app.mount('/', StaticFiles(directory='static', html=True), name='str')

@app.get('/', response_class=HTMLResponse)
async def get_root(request: Request) -> HTMLResponse:
    return HTMLResponse('index.html')

app_api.include_router(auth_router)
app_api.include_router(tweet_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', post=8000, reload=True)
