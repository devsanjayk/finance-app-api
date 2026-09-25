from fastapi import APIRouter

router = APIRouter(tags=["health"])

@router.get("/")
def read_root():
    return {"message": "Hello World !"}

@router.get("/health")
def get_health():
    return {"status": "Ok"}