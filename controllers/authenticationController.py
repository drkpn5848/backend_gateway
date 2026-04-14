from fastapi import APIRouter
from models.schemas import SigninSchema, SignupSchema

router = APIRouter(prefix="/authservice")

@router.post("/signup")
async def signup(U: SignupSchema):
    return{
        "code": 200,
        "message": U
    }

@router.post("/signin")
async def signin(U: SigninSchema):
    return{
        "code": 200,
        "message": U
    }
