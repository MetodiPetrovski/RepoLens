#!pip install sentence-transformers
#!pip install faiss-cpu
import faiss

from sentence_transformers import SentenceTransformer

from ingestion.git_loader import clone_repo
from ingestion.file_scanner import scan_repository, load_files
from parser.ast_extractor import extract_ast_chunks
from embeddings.semantic_formatter import chunk_to_text


def build_repo_index(url):

    repo_path = clone_repo(url, "temp_repo")

    files = scan_repository(repo_path)

    docs = load_files(files)

    print(f"Loaded {len(docs)} files")

    chunks = extract_ast_chunks(docs)

    embedding_docs = [
        chunk_to_text(chunk)
        for chunk in chunks
    ]

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

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

    return model, index, embedding_docs
