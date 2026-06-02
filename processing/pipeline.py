from parsing.python_ast import parse_python_code


def enrich_with_ast(docs):

    enriched = []

    for doc in docs:

        try:
            ast_info = parse_python_code(doc["content"])

            enriched.append({
                "path": doc["path"],
                "content": doc["content"],
                "ast": ast_info
            })

        except Exception as e:
            print(f"AST failed for {doc['path']}")

    return enriched
