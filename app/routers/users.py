from fastapi import APIRouter, HTTPException, status
from starlette.responses import JSONResponse
from app.database.utils import get_user_by_id, check_follow_user_ability
from app.schemas.base_schema import DefaultSchema

router = APIRouter(prefix="/api", tags=["users"])


@router.get("/users/me", status_code=status.HTTP_200_OK)
async def get_info_about_me(current_user):
    user = dict()
    user["id"] = current_user.id
    user["name"] = current_user.username
    all_followers = list()
    followers = current_user.followers
    for follower in followers:
        follower_user = dict()
        follower_user["id"] = follower.id
        follower_user["name"] = follower.username
        all_followers.append(follower_user)
    user["followers"] = all_followers
    all_followings = list()
    followings = current_user.following
    for following in followings:
        following_user = dict()
        following_user["id"] = following.id
        following_user["name"] = following.username
        all_followings.append(following_user)
    user["followings"] = all_followings
    answer = dict()
    answer["user"] = user
    answer["result"] = True
    return JSONResponse(content=answer, status_code=200)


@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def get_info_of_user_by_id(user_id: int, session):
    user_ = await get_user_by_id(user_id, session)
    user = dict()
    user["id"] = user_.id
    user["name"] = user_.username
    all_followers = list()
    followers = user_.followers
    for follower in followers:
        follower_user = dict()
        follower_user["id"] = follower.id
        follower_user["name"] = follower.username
        all_followers.append(follower_user)
    user["followers"] = all_followers
    all_followings = list()
    followings = user_.following
    for following in followings:
        following_user = dict()
        following_user["id"] = following.id
        following_user["name"] = following.username
        all_followings.append(following_user)
    user["followings"] = all_followings
    answer = dict()
    answer["result"] = True
    answer["user"] = user
    return JSONResponse(content=answer, status_code=200)


@router.post('/users/{user_id}/follow', status_code=status.HTTP_201_CREATED, response_model=DefaultSchema, )
async def follow_user(user_id, current_user, session):
    user_to_follow = await get_user_by_id(user_id, session)
    following_ability = await check_follow_user_ability(current_user, user_to_follow)
    if following_ability:
        user_to_follow.followers.append(current_user)
        await session.commit()
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Вы уже подписаны на этого пользователя!",)
    return {"result": True}


@router.delete("/users/{user_id}/follow", status_code=status.HTTP_200_OK, response_model=DefaultSchema,)
async def unsubscribe_from_user(user_id: int, current_user, session,):
    follower_deleted = await get_user_by_id(user_id, session)

    if follower_deleted not in current_user.following:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Вы не подписаны на этого пользователя.",)
    current_user.following.remove(follower_deleted)
    await session.commit()
    return {"result": True}
