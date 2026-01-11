from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_classic.chains import RetrievalQA


EMBEDDING_MODEL = "nomic-embed-text"
VECTORDB_DIR = "./chroma_store"
QUERY_MODEL = "llama3.1:8b"
QUERY_TEMPERATURE = 0.2


qa_llm = Ollama(
    model=QUERY_MODEL,
    temperature=QUERY_TEMPERATURE
)

embeddings = OllamaEmbeddings(
    model=EMBEDDING_MODEL
)

vectordb = Chroma(
    persist_directory=VECTORDB_DIR,
    embedding_function=embeddings
)

retriever = vectordb.as_retriever(
    search_kwargs={
        "k": 6,
        "filter": {
            "importance_score": {"$gte": 0.3}
        }
    }
)

qa = RetrievalQA.from_chain_type(
    llm=qa_llm,
    retriever=retriever,
    return_source_documents=True
)


query = input("Enter your query:\n")

response = qa(query)
print(response["result"])