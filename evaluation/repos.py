from pathlib import Path

BASE_DIR = Path(__file__).parent



REPOSITORIES = [
    
  {
        "name": "strix",
        "url": "https://github.com/usestrix/strix.git",
        "benchmark": BASE_DIR / "benchmarks" / "strix.json",
    }
]
