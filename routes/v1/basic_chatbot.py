from llm.groq_chat_model import gpt_oss_120b as GroqModel
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, APIRouter


route = APIRouter()

@route.get("/basic_chat_bot")
def call_model(message:str):
    while 1==1:
        user_input = message
        if user_input in ["quit","exit","q"]:
            break 
        response = GroqModel.invoke(user_input)
        return response.content
    