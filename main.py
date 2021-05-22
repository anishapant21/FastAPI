from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def index(limit, published: bool=True, sort: Optional[str]=None):
    if published:
        return { 'data' : f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('post/new')
def new():
    return {'data': 'published blogs'}

@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    #fetch comments of the blog with id=id
    return {'data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    published_at :Optional[bool]

#test with docs
@app.post('/blog')
def create_blog(request: Blog):
    return {'data': "Blog is created with title as {request.title}"}