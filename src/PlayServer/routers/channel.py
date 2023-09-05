from fastapi import APIRouter

router = APIRouter()


@router.post("/channel", tags=["channel"])
async def create_channel():
    pass


@router.get("/channel/{channel}", tags=["channel"])
async def get_channel(channel: int):
    pass


@router.patch("/channel/{channel}", tags=["channel"])
async def update_channel(channel: int):
    pass


@router.delete("/channel/{channel}", tags=["channel"])
async def delete_channel(channel: int):
    pass


@router.post("/channel/{channel}/user", tags=["channel", "user"])
async def add_user(channel: int):
    pass


@router.delete("/channel/{channel}/user/{user}", tags=["channel", "user"])
async def delete_user(channel: int, user: int):
    pass
