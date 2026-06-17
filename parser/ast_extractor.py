from parser.ast_parser import parse_python_file


def extract_ast_chunks(docs):
    all_chunks = []
    python_files = 0

    for doc in docs:

        path = doc["path"]
        content = doc["content"]

        if not path.endswith(".py"):
            continue

        python_files += 1

        try:
            chunks = parse_python_file(content, path)
            all_chunks.extend(chunks)

        except Exception as e:
            print(f"Failed on {path}: {e}")

    print("Python files parsed:", python_files)
    print("Total AST chunks:", len(all_chunks))

    return all_chunks
