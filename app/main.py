from fastapi import FastAPI, status

app = FastAPI()


@app.post('/')
async def main():
    return {'msg': 'ok'}


@app.get('/healthcheck', status_code=status.HTTP_200_OK)
async def healthcheck():
    return {'msg': 'ok'}
