from ingestion.git_loader import clone_repo
from ingestion.file_scanner import scan_repository, load_files

from parser.ast_extractor import extract_ast_chunks
from embeddings.semantic_formatter import chunk_to_text

# Need to install !pip install sentence-transformers
from sentence_transformers import SentenceTransformer

# Need to install !pip install faiss-cpu
from retrieval.search import search_repo

def main():

    url = "https://github.com/psf/requests.git"

    repo_path = clone_repo(url, "temp_repo")

    files = scan_repository(repo_path)

    docs = load_files(files)

    print(f"Loaded {len(docs)} files")

    chunks = extract_ast_chunks(docs)
    embedding_docs = [
    chunk_to_text(chunk)
    for chunk in chunks
]
    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = model.encode(
    embedding_docs,
    show_progress_bar=True,
    convert_to_numpy=True
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

faiss.normalize_L2(embeddings)

index.add(embeddings)

assert index.ntotal == len(embedding_docs)
embeddings[:50]

results = search_repo(
    "How are HTTP redirects handled?",
    model,
    index,
    embedding_docs
)

for r in results:
    print(r["score"])
    print(r["text"][:500])

 

if __name__ == "__main__":
    main()
