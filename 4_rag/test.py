from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()
current_dir = os.path.dirname(os.path.abspath(__file__))
temp_dir = os.path.join(current_dir, "temp_chroma_db")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Create empty Chroma DB
db = Chroma(persist_directory=temp_dir, embedding_function=embeddings)

# Add a dummy doc to test
docs = ["This is a test document about MRI coverage."]
metadatas = [{"source": "dummy"}]
db.add_texts(docs, metadatas=metadatas)

# Try retrieval
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 1})
results = retriever.get_relevant_documents("Do I have coverage for 3 MRIs?")
for r in results:
    print(r.page_content)
