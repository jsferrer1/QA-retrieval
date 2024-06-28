from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings

print("Loading documents")
loader = DirectoryLoader("./bible", glob="**/*.docx")
books = loader.load()
print(len(books))

print("Splitting into chunks")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(books)
print(type(all_splits))
print(len(all_splits))

print("Storing in ChromaDB")
vectorstore = Chroma.from_documents(
    documents=all_splits,
    embedding=OllamaEmbeddings(model="llama3", show_progress=True),
    persist_directory="./chroma_db",
)