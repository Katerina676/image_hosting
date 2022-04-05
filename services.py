from uuid import uuid4

import aiofiles
from fastapi import UploadFile, HTTPException, BackgroundTasks

from models import Image
from schemas import UploadImg


async def write_img(file_name: str, file: UploadFile):
    async with aiofiles.open(file_name, "wb") as buffer:
        data = await file.read()
        await buffer.write(data)


async def save_img(
        file: UploadFile,
        user: int,
        background_tasks: BackgroundTasks,
        title: str,
        description: str
                   ):
    file_name = f'media/{file.filename}'
    if file.content_type == 'image/jpg' or 'image/png':
        background_tasks.add_task(write_img, file_name, file)
    else:
        raise HTTPException(status_code=418, detail='it is not jpg/png')
    info = UploadImg(title=title, description=description)
    return await Image.objects.create(file=file.filename, user=user, **info.dict())