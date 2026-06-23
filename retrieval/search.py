import faiss

def search_repo(
    question,
    model,
    index,
    embedding_docs,
    k=5
):
    query_embedding = model.encode(
        [question],
        convert_to_numpy=True
    ).astype("float32")

    faiss.normalize_L2(query_embedding)

    scores, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for score, idx in zip(scores[0], indices[0]):
        results.append({
            "score": float(score),
            "text": embedding_docs[idx]
        })

    return results
