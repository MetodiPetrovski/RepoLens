import json
from retrieval.search import search_repo


def evaluate(model, index, embedding_docs, benchmark_path):
    with open(benchmark_path, "r", encoding="utf-8") as f:
        benchmark = json.load(f)

    top1_correct = 0
    top3_correct = 0
    top5_correct = 0

    print("=" * 60)
    print("RepoLens Evaluation")
    print("=" * 60)

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
            r["text"].lower()
            for r in results
        ]

        found = False

        if expected.lower() in retrieved[0]:
            top1_correct += 1
            top3_correct += 1
            top5_correct += 1
            found = True

        elif any(expected.lower() in r for r in retrieved[:3]):
            top3_correct += 1
            top5_correct += 1
            found = True

        elif any(expected.lower() in r for r in retrieved):
            top5_correct += 1
            found = True

        print()
        print(f"Question : {question}")
        print(f"Expected : {expected}")
        print("Result   :", "PASS" if found else "FAIL")

    total = len(benchmark)

    print("\n" + "=" * 60)
    print("Evaluation Summary")
    print("=" * 60)

    print(f"Questions : {total}")
    print(f"Top-1 Accuracy : {top1_correct}/{total} ({100*top1_correct/total:.1f}%)")
    print(f"Top-3 Accuracy : {top3_correct}/{total} ({100*top3_correct/total:.1f}%)")
    print(f"Top-5 Accuracy : {top5_correct}/{total} ({100*top5_correct/total:.1f}%)")
