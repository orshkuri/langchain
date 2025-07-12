from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# Load env variables from .env
load_dotenv()

# Antropic Chat Model example
model = ChatOpenAI(model="calude-3-opus-20240229")

messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?")
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI:{result.content}")
