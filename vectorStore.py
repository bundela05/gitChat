from chunker import all_chunks
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents =all_chunks,
    embedding=embeddings,
    persist_directory='chroma_db',
    collection_name="sample"
)
print("added all_chunks to the vector store")

# print(vectorstore.get(include=["embeddings"]))
# print(vectorstore._collection.count())
# print(vectorstore.get_by_ids(['7462fe19-083b-497e-a248-40bb769c025f']))