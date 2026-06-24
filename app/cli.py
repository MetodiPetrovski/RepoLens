from indexing.repo_index import build_repo_index
from llm.chat import chat_loop


def main():

    url = input(
        "GitHub URL > "
    )

    model, index, embedding_docs = (
        build_repo_index(url)
    )

    chat_loop(
        model,
        index,
        embedding_docs,
        debug=True
    )


if __name__ == "__main__":
    main()
