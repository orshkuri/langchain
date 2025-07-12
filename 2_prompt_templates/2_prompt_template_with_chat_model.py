from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

# PART 1
# print("---Prompt from Template---")
# template = "Tell me a joke about {topic}."
# prompt_template = ChatPromptTemplate.from_template(template)

# prompt = prompt_template.invoke({"topic": "cats"})
# result = model.invoke(prompt)
# print(result.content)

# PART 2 
messages = {
    ("system", "You are a comedian who tells joke about {topic}."),
    ("human", "Tell me {joke_count} jokes.")
}
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
result = model.invoke(prompt)
print(result.content)
