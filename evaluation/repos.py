from pathlib import Path

BASE_DIR = Path(__file__).parent



REPOSITORIES = [
    
  {
        "name": "strix",
        "url": "https://github.com/usestrix/strix.git",
        "commit": "3b79e97f000aa65461e61839c647a70f7e754554",
        "benchmark": BASE_DIR / "benchmarks" / "strix.json",
    }
]
