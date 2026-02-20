from pathlib import Path

from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_classic.chains import RetrievalQA

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
CHROMA_DIR = PROJECT_ROOT / "chroma_db"

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Carregar banco
vectorstore = Chroma(
    persist_directory=str(CHROMA_DIR),
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# Modelo local
llm = Ollama(
    model="phi3",
    system="Você é um assistente que responde sempre em português do Brasil." \
    "Responda EXCLUSIVAMENTE em português do Brasil. Não responda em inglês."
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

while True:
    pergunta = input("\nPergunta: ")

    if pergunta.lower() == "sair":
        break
    
    resposta = qa_chain.run(pergunta)
    print("\nResposta:", resposta)