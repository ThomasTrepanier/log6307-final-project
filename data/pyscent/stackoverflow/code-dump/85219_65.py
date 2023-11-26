from fastapi import APIRouter

router = APIRouter()

@router.get("/some")
async def some_path():
    pass

@router.get("/path")
async def some_other_path():
    pass

@router.post("/some_post_path")
async def some_post_path():
    pass
