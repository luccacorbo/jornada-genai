import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Carregar todos os .md manualmente
documents = []

for filename in os.listdir("data"):
    if filename.endswith(".md"):
        loader = TextLoader(os.path.join("data", filename), encoding="utf-8")
        documents.extend(loader.load())

print(f"{len(documents)} documentos carregados.")

# Dividir em chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

print(f"{len(docs)} chunks criados.")

# Embeddings locais
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Criar banco vetorial
vectorstore = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="./chroma_db"
)

vectorstore.persist()

print("Ingestão finalizada com sucesso!")
