from typing import Annotated

from app.database.database import async_get_db
from fastapi import APIRouter, Depends, HTTPException, UploadFile, status
from app.models.media import Media
from app.models.users import User
from app.schemas.media_schema import MediaUpload
from sqlalchemy.ext.asyncio import AsyncSession
# from utils.auth import authenticate_user
from app.utils.file_utils import save_uploaded_file, MEDIA_PATH

router = APIRouter(prefix="/api", tags=["media_v1"])


@router.post(
    "/medias", status_code=status.HTTP_201_CREATED, response_model=MediaUpload
)
async def upload_media(file: UploadFile, user, session: AsyncSession = Depends(async_get_db),):
    try:
        file = await save_uploaded_file(file)
        new_media = Media(media_path=file)
        session.add(new_media)
        await session.commit()

        return new_media
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)
        )
