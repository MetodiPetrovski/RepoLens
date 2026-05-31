import os
def scan_repository(repo_path):
    files = []

    for root, dirs, filenames in os.walk(repo_path):

        dirs[:] = [
            d for d in dirs
            if d not in [".git", "__pycache__", "venv"]
        ]

        for filename in filenames:

            if filename.endswith(".py"):

                full_path = os.path.join(root, filename)

                files.append(full_path)

    return files


def load_files(file_paths):

    documents = []

    for path in file_paths:

        try:

            with open(path, "r", encoding="utf-8") as f:

                content = f.read()

                documents.append({
                    "path": path,
                    "content": content
                })

        except Exception as e:

            print(f"Failed: {path}")

    return documents
