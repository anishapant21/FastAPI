from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return { 'key' : 'value'}


@app.get('/about')
def about():
    return {'data': {'about page'}}