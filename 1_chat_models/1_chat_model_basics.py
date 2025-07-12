from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# load env variables from .env
load_dotenv()

# Create ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")

result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
