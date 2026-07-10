from indexing.repo_index import build_repo_index
from evaluation.evaluator import evaluate


url = "https://github.com/usestrix/strix.git"

model, index, embedding_docs = build_repo_index(url)

evaluate(
    model,
    index,
    embedding_docs,
    "benchmarks/strix.json"
)
