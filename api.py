from fastapi import APIRouter, UploadFile, File, Form, HTTPException, BackgroundTasks
from starlette.responses import StreamingResponse
from models import Image, User
from schemas import Message, UploadImg
from services import save_img
from uuid import uuid4

file_router = APIRouter()


@file_router.post("/")
async def create_img(
        background_tasks: BackgroundTasks,
        title: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(...)
                    ):
    user = await User.objects.first()
    return await save_img(file, user.dict().get('id'), background_tasks, title, description)


@file_router.get("/file/{file_pk}", responses={404: {"model": Message}})
async def get_file(file_pk: int):
    file = await Image.objects.select_related('user').get(pk=file_pk)
    file_like = open(f'media/{file.dict().get("file")}', mode="rb")
    return StreamingResponse(file_like, media_type="image/jpg")



