from typing import Optional
from fastapi import FastAPI, Response, status
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

def find_post(id):
    for post in my_posts:
        print (post['id'])
        if post['id'] == int(id):
            return post
    return None

@app.get("/")
def root():
    return {"message": "Welcome to my API!"}

# best practice: endpoints should be plural 
@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    print(id)
    post_found = find_post(id)
    if not post_found:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"post with id: {id} was not found."}
    return {"post_detail": post_found} 

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    new_id = abs(hash(post_dict['title']+post_dict['content']+str(randint(1,1000))))
    post_dict['id'] = new_id

    my_posts.append(post_dict)
    return {"content":post_dict}
