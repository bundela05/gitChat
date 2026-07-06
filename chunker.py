from gitHubLoader import documents
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from pathlib import Path

language_map = {
    ".py": Language.PYTHON,
    ".md": Language.MARKDOWN,
    ".html": Language.HTML,
    ".go": Language.GO,
    ".java": Language.JAVA,
    ".cpp": Language.CPP,
    ".php": Language.PHP,
    ".r": Language.RST,   # There is no Language.R
    ".rs": Language.RUST,
    ".c": Language.C,
}

all_chunks = []
for doc in documents:
    extension = Path(doc.metadata["source"]).suffix.lower()
    language = language_map.get(extension)

    if language:
        splitter = RecursiveCharacterTextSplitter.from_language(
            language=language,
            chunk_size = 1000,
            chunk_overlap = 200,
        )
    else: 
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 200,
        )
    chunks = splitter.split_documents([doc])
    all_chunks.extend(chunks)

print("chunks formed")
