from langchain_ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings


def get_embedding_function():
    # Usar Ollama por defecto
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
