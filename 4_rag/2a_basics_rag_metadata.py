import os
from dotenv import load_dotenv

# from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

load_dotenv()

# Define the directory containing the text file and the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
books_dir = os.path.join(current_dir, "books")
persistent_directory = os.path.join(current_dir, "db", "faiss_db_with_metadata")

# Check if the Chroma vector store already exists
if not os.path.exists(persistent_directory):
    print("Persistent directory does not exist. Initializing vector store...")

    # Ensure the text file books_dir
    if not os.path.exists(books_dir):
        raise FileNotFoundError(
            f"The Directory {books_dir} does not exist. Please check the path."
        )
    
    book_files = [f for f in os.listdir(books_dir) if f.endswith(".txt")]
    # print(book_files)

    # Read the text content from each file and store it with metadata
    documents = []
    for book_file in book_files:
        file_path = os.path.join(books_dir, book_file)
        # print(file_path)
        loader = TextLoader(file_path, encoding="utf-8")
        book_docs = loader.load()
        for doc in book_docs:
            print(book_file)
            doc.metadata = {"source": book_file}
            documents.append(doc)

    # Split the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    print(f"Number of document chunks: {len(docs)}")

    print("\n-- Creating Embeddings --\n")
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vectore_store = FAISS.from_documents(documents=docs, embedding=embeddings)

    # Save the vector store
    vectore_store.save_local(persistent_directory)    
