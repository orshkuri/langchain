from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage


# PART 1
# template = "Tell me a joke about {topic}."
# prompt_message = ChatPromptTemplate.from_template(template)

# print("---Prompt from template")
# prompt = prompt_message.invoke({"topic": "cats"})
# print(prompt)

# PART 2
# template_multiple = """You are a helpful assistant.
# Human: Tell me a {adjective} story about a {animal}.
# Assistant:"""

# prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
# prompt = prompt_multiple.invoke({"adjective": "funny", "animal": "panda"})
# print("\n--- Prompt with multiple Placeholders ---\n")
# print(prompt)

# PART 3
messages = {
    ("system", "You are a comedian who tells joke about {topic}."),
    ("human", "Tell me {joke_count} jokes.")
}
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
print("\n--- Prompt with System and Human messages (Tuple) ---\n")
print(prompt)