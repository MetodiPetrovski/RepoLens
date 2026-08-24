import json
from pathlib import Path


HISTORY_FILE = Path(__file__).parent / "history.json"


def save_evaluation(result):

    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
    else:
        history = {
            "experiments": []
        }

    history["experiments"].append(result)

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(
            history,
            f,
            indent=4
        )
