from .v1.basic_chatbot import call_model as Chat_Model 
from fastapi import APIRouter
from .v1.basic_chatbot import route


router = APIRouter()
router.include_router(route,prefix="/version1")
 
