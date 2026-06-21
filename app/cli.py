from ingestion.git_loader import clone_repo
from ingestion.file_scanner import scan_repository, load_files

from parser.ast_extractor import extract_ast_chunks
from embeddings.semantic_formatter import chunk_to_text



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

embedding_docs[:100]


if __name__ == "__main__":
    main()
