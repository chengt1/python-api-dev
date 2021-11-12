from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randint

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
 
my_posts = [{"title":"title1", "content": "beach", "id": 1}, 
{"title":"Europe", "content": "europe is fun!", "id":2}]

@app.get("/")
def root():
    return {"message": "Welcome to my API!"}

# best practice: endpoints should be plural 
@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post():
    return

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    new_id = abs(hash(post_dict['title']+post_dict['content']+str(randint(1,1000))))
    post_dict['id'] = new_id

    my_posts.append(post_dict)
    return {"content":post_dict}
