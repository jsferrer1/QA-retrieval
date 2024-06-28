from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader("./bible", glob="**/*.docx")
books = loader.load()
print(len(books))
