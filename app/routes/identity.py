# app/routes/user.py
import fastapi

router = fastapi.APIRouter()

@router.get("/")
async def read_users():
    return {"message": "Get all users"}
