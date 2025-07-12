from langchain_community.document_loaders import UnstructuredPDFLoader

file_path = "hebrew_policy.pdf"
loader = UnstructuredPDFLoader(file_path)
print('now')

docs = loader.load()
print('now')

print(docs[0].metadata)
