from pathlib import Path

BASE_DIR = Path(__file__).parent



REPOSITORIES = [
    
  {
        "name": "strix",
        "url": "https://github.com/usestrix/strix.git",
        "commit": "e152c4c7c037a895b039d5fbdf469ac7b17a5ee9",
        "benchmark": BASE_DIR / "benchmarks" / "strix.json",
    }
]
