from langchain_cohere import  Cohere

llm = Cohere()
response = llm.invoke("What is the capital of India?")
print(response)