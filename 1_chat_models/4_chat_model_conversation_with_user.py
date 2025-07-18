from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

chat_history = []  # Use a list to store messages

# Set an initial system message (optional)
system_message = SystemMessage(content="אתה עוזר AI מועיל")
chat_history.append(system_message)

# Chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))  # Add user message

    # Get AI response using history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print(f"AI: {response}")

print("--- Message History ---")
print(chat_history)
