from fastapi import APIRouter

router = APIRouter()


@router.get("/auth", tags=["auth"])
async def check_auth():
    pass


@router.post("/auth", tags=["auth"])
async def login():
    pass


@router.delete("/auth", tags=["auth"])
async def logout():
    pass
