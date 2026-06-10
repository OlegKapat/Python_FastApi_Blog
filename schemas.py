from pydantic import BaseModel, ValidationError, Field, ConfigDict,EmailStr
from datetime import datetime


class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr = Field( max_length=120)

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=200)

class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    image_path: str 
    image_file: str | None

class UserPrivate(UserPublic):
    email: EmailStr

class UserUpdate(BaseModel):
    username: str | None = Field(default=None,  min_length=3, max_length=50)
    email: EmailStr | None = Field(default=None, max_length=120)
    

class Token(BaseModel):
    access_token: str
    token_type: str

class PostUpdate(BaseModel):
     title: str | None = Field(default=None, min_length=2, max_length=100)
     content: str | None = Field(default=None, min_length=1)

class PostBase(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    content: str = Field(min_length=1)

class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    date_posted: datetime
    author: UserPublic


class PaginatedPostsResponse(BaseModel):
    posts: list[PostResponse]
    total: int
    skip: int
    limit: int
    has_more: bool
