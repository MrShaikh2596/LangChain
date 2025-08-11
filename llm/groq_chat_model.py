from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

gpt_oss_120b = ChatGroq(model="openai/gpt-oss-120b")
gpt_oss_20b = ChatGroq(model="openai/gpt-oss-20b")