from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

groq_chat_model = ChatGroq(model="openai/gpt-oss-120b")
