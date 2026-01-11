Assignment Problem Statement:


Create an agent of your choice that automates a problem in any field you prefer. The agent’s control flow should be determined by an LLM (Large Language Model).




Assignment Planning:

The task as I understand is to create a solution, in which using an LLM is integral to its logic.

I will be using a model from Ollama - free.

Agent chosen function - Be able to query upon a large collection of files (valid types: pdf, word, csv, txt, json, python)

Use of LLM: For creation of metadata while creating documents for RAG model

I will also add RAG evaluation functions to test for production ready



Dependencies:

Make sure to install Ollama in your machine as this uses LLM models from Ollama

Run the following commands to install dependencies:

(if pip does not work try pip3 or another method to install this python libraries)

pip install chromadb

pip install sentence-transformers

pip install pypdf

pip install langchain-community

pip install langchain

pip install langchain-core

pip install langchain-classic

pip install tf-keras



Commands to run before running the file:

ollama pull qwen2.5:7b

ollama pull llama3.1:8b

ollama pull nomic-embed-text



To verify, run ollama list and ensure you see nomic-embed-text:latest, llama3.1:8b, and qwen2.5:7b



To be able to query on your pdf file, follow the following steps:



Step 1:

In the rag_ingestion.py file, change FILE_PATH to the path of your pdf file (sample.pdf file is provided in case you want to test out the model)

You may choose your ollama ingestion and embedding model by changing the INGESTION_MODEL and EMBEDDING_MODEL variables. But if you do, remember to run ollama pull model-name



Step 2:

Run the command: python3 rag_ingestion.py

Wait until it prints "Ingestion completed"



Step 3:

In the rag_retrieval.py file, change EMBEDDING_MODEL to match the rag_ingestion.py file

You may choose your ollama query model by changing the QUERY_MODEL variable. But if you do, remember to run ollama pull model-name



Step 4:

Run the command: python3 rag_retrieval.py

You will be prompted to enter a query, this is the question you may want to ask about your file

The result will be printed after it is completely received



Step 5:

If you want to query again, repeat step 4





Next Steps for this project:



Step 1:

Add ingestion capabilites for word, csv, txt, json, and python files



Step 2:

Add ingestion capability for multiple files at once



Step 3:

Parallelize ingestion



Step 4:

Parallelize retrieval





Test run:

I tested the code by using the sample.pdf file provided. 

Query given was: "What are Kartik's main skills?"

Output was as follows:

Based on the provided text, Kartik's main skills appear to be:



1. Artificial Intelligence (AI)
2. Machine Learning (ML)
3. Python programming
4. PyTorch
5. Prompt engineering
6. LLM APIs (Large Language Model Application Programming Interfaces)
7. Data preprocessing and feature engineering
8. Model building, evaluation, and refinement



Additionally, Kartik has earned various certifications in AI and cloud computing, including:


1. IBM AI Developer Certificate
2. AWS AI Practitioner Certificate
3. AWS Cloud Practitioner Certification
4. Azure Certification
