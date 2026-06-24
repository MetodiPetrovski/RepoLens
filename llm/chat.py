from retrieval.search import search_repo
from llm.generator import generate_answer
from llm.prompt_builder import (
    build_context,
    create_prompt
)


def chat_loop(
    model,
    index,
    embedding_docs,
    debug=False
):

    print("RepoLens Chat")
    print("Type 'exit' to quit")

    while True:

        question = input(
            "\nAsk RepoLens > "
        )

        if question.lower() == "exit":
            break

        results = search_repo(
            question,
            model,
            index,
            embedding_docs
        )

        if debug:

            print("\nRetrieved Chunks:")

            for i, r in enumerate(results):

                print(
                    f"{i+1}. score={r['score']:.3f}"
                )

        answer = generate_answer(
            question,
            results,
            create_prompt,
            build_context
        )

        print("\nAnswer:\n")
        print(answer)
