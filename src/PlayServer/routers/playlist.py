from fastapi import APIRouter

router = APIRouter()


@router.post("/playlist", tags=["playlist"])
async def create_playlist():
    pass


@router.get("/playlist/{playlist}", tags=["playlist"])
async def get_playlist(playlist: int):
    pass


@router.patch("/playlist/{playlist}", tags=["playlist"])
async def update_playlist(playlist: int):
    pass


@router.delete("/playlist/{playlist}", tags=["playlist"])
async def delete_playlist(playlist: int):
    pass


@router.post("/playlist/{playlist}/item", tags=["playlist", "item"])
async def add_item(playlist: int):
    pass


@router.patch("/playlist/{playlist}/item/{item}", tags=["playlist", "item"])
async def update_item(playlist: int, item: int):
    pass


@router.delete("/playlist/{playlist}/item/{item}", tags=["playlist", "item"])
async def delete_item(playlist: int, item: int):
    pass
