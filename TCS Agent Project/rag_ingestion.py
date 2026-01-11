from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import Ollama
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_classic.prompts import PromptTemplate
import time


FILE_PATH = "sample.pdf"
DOC_CHUNK_SIZE = 800
DOC_CHUNK_OVERLAP = 150
INGESTION_MODEL = "qwen2.5:7b"
EMBEDDING_MODEL = "nomic-embed-text"
VECTORDB_DIR = "./chroma_store"


def normalize_metadata(meta: dict) -> dict:
    clean = {}
    for key, value in meta.items():
        if isinstance(value, list):
            clean[key] = ", ".join(map(str, value))
        elif isinstance(value, dict):
            clean[key] = str(value)
        else:
            clean[key] = value
    return clean


loader = PyPDFLoader(FILE_PATH)
docs = loader.load()

# print("File loaded")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=DOC_CHUNK_SIZE,
    chunk_overlap=DOC_CHUNK_OVERLAP
)
docs = splitter.split_documents(docs)

# print("Docs created")
# print("Num: ", len(docs))


metadata_llm = Ollama(
    model=INGESTION_MODEL,
    temperature=0
)

prompt = PromptTemplate(
    input_variables=["chunk", "prev", "next"],
    template="""
You are annotating a document chunk for retrieval.

Chunk:
{chunk}

Previous:
{prev}

Next:
{next}

Return valid JSON with:
summary
chunk_type
importance_score
main_topics
prev_relation
next_relation
"""
)


metadata_chain = prompt | metadata_llm | JsonOutputParser()

# print("Creating metadata")

for i, doc in enumerate(docs):
    # print("Working on doc", i + 1)
    # start = time.time()
    meta = metadata_chain.invoke({
        "chunk": doc.page_content,
        "prev": docs[i-1].page_content if i > 0 else "None",
        "next": docs[i+1].page_content if i < len(docs)-1 else "None"
    })

    meta = normalize_metadata(meta)
    meta["position"] = i
    doc.metadata.update(meta)

    # print("Time taken:", time.time() - start)

# print("Metadata created")


embeddings = OllamaEmbeddings(
    model=EMBEDDING_MODEL
)

vectordb = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory=VECTORDB_DIR
)

# print("Stored in vector DB")

vectordb.persist()
print("Ingestion complete")