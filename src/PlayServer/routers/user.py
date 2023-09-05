from fastapi import APIRouter

router = APIRouter()


@router.get("/user", tags=["user"])
async def get_user():
    pass


@router.post("/user", tags=["user"])
async def create_user():
    pass


@router.patch("/user", tags=["user"])
async def update_user():
    pass


@router.delete("/user", tags=["user"])
async def delete_uesr():
    pass
