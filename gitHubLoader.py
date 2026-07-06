# from langchain_community.document_loaders import GithubFileLoader
from langchain_community.document_loaders import TextLoader, DirectoryLoader
import os      #for directory management
from git import Repo

repo_url = "https://github.com/arnav-terex/ReDocs"
local_dir = "./my_local_repo"

try:
    cloned_repo = Repo.clone_from(repo_url, local_dir)
    print(f"Success! Cloned to: {cloned_repo.working_dir}")
except Exception as e:
    print(f"Error during cloning: {e}")

# if not os.path.exists(local_dir):
#     Repo.clone_from(repo_url,local_dir)
#     print("repository cloned.")
# else :
#     print("repository already exist")

text_extensions = [
    # JavaScript / TypeScript / Web
    "js", "jsx", "ts", "tsx", "html", "htm", "css", "scss", "sass", "less", 
    "json", "xml", "ejs", "twig", "hbs", "jsp", "asp", "aspx",

    # Python / Data Science
    "py", "r", "rmd", "ipynb",

    # C / C++ / C# / Java Ecosystem
    "java", "cpp", "cc", "cxx", "h", "hpp", "cs", "kt", "kts", "scala",

    # Modern Backend & Systems
    "go", "rs", "swift", "dart", "lua", "rb", "php", "pl", "pm", "sql",

    # Shell & Scripts
    "sh", "bash", "zsh", "bat", "ps1",

    # Configuration & Data
    "yaml", "yml", "toml", "ini", "conf", "config", "env", "lock", "properties", "csv", "tsv",

    # Documentation & Markup
    "md", "markdown", "rst", "txt", "tex", "asciidoc", "adoc"
]

documents = []
for ext in text_extensions:
    loader = DirectoryLoader(
        local_dir,
        glob = f"**/*.{ext}",
        loader_cls=TextLoader,
        silent_errors = True,
        recursive = True
    )
    documents.extend(loader.load())

print(len(documents))

import shutil
shutil.rmtree(local_dir)            # my_local_repo is no longer needed so delete it
print("Local repository deleted.")
