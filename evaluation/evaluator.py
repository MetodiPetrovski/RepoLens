import json
from datetime import datetime

from evaluation.repos import REPOSITORIES
from indexing.repo_index import build_repo_index
from retrieval.search import search_repo


def evaluate_repository(
    repo_name,
    model,
    index,
    embedding_docs,
    benchmark_path
):
    """
    Evaluate one repository.
    """

    with open(benchmark_path, "r", encoding="utf-8") as f:
        benchmark = json.load(f)

    top1 = 0
    top3 = 0
    top5 = 0

    failures = []

    print("\n" + "=" * 70)
    print(f"Evaluating: {repo_name}")
    print("=" * 70)


    for test in benchmark:

        question = test["question"]
        expected = test["expected"]

        results = search_repo(
            question,
            model,
            index,
            embedding_docs,
            k=5
        )


        retrieved = [
            r["text"]
            for r in results
        ]

        retrieved_lower = [
            r.lower()
            for r in retrieved
        ]


        passed = False


        if expected.lower() in retrieved_lower[0]:
            top1 += 1
            top3 += 1
            top5 += 1
            passed = True


        elif any(expected.lower() in r for r in retrieved_lower[:3]):
            top3 += 1
            top5 += 1
            passed = True


        elif any(expected.lower() in r for r in retrieved_lower):
            top5 += 1
            passed = True



        if not passed:

            failures.append(
                {
                    "question": question,
                    "expected": expected,
                    "retrieved": retrieved
                }
            )


        print(
            f"{'PASS' if passed else 'FAIL'} | {question}"
        )


    total = len(benchmark)


    return {
        "repository": repo_name,
        "questions": total,
        "top1": top1,
        "top3": top3,
        "top5": top5,
        "top1_accuracy": top1 / total,
        "top3_accuracy": top3 / total,
        "top5_accuracy": top5 / total,
        "failures": failures
    }



def run_evaluation():

    experiment_name = input(
        "Experiment name: "
    )

    description = input(
        "Experiment description: "
    )


    print("\nStarting evaluation...")
    

    experiment_results = {
        "name": experiment_name,
        "description": description,
        "date": str(datetime.now()),
        "repositories": []
    }


    overall_top1 = 0
    overall_top3 = 0
    overall_top5 = 0
    overall_questions = 0



    for repo in REPOSITORIES:

        print(
            f"\nLoading repository: {repo['name']}"
        )


        model, index, embedding_docs = build_repo_index(
            repo["url"]
        )


        result = evaluate_repository(
            repo["name"],
            model,
            index,
            embedding_docs,
            repo["benchmark"]
        )


        experiment_results["repositories"].append(
            result
        )


        overall_top1 += result["top1"]
        overall_top3 += result["top3"]
        overall_top5 += result["top5"]

        overall_questions += result["questions"]



    experiment_results["overall"] = {
        "questions": overall_questions,
        "top1_accuracy": overall_top1 / overall_questions,
        "top3_accuracy": overall_top3 / overall_questions,
        "top5_accuracy": overall_top5 / overall_questions,
    }



    print("\n")
    print("=" * 70)
    print("FINAL EVALUATION SUMMARY")
    print("=" * 70)


    print(
        f"Repositories evaluated: {len(REPOSITORIES)}"
    )

    print(
        f"Questions: {overall_questions}"
    )

    print(
        f"Top-1 Accuracy: {overall_top1/overall_questions:.2%}"
    )

    print(
        f"Top-3 Accuracy: {overall_top3/overall_questions:.2%}"
    )

    print(
        f"Top-5 Accuracy: {overall_top5/overall_questions:.2%}"
    )


    return experiment_results



if __name__ == "__main__":
    run_evaluation()