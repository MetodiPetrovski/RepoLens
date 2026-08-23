from pathlib import Path

BASE_DIR = Path(__file__).parent



REPOSITORIES = [
    
  {
        "name": "strix",
        "url": "https://github.com/usestrix/strix.git",
        "commit": "1c499c5b2d788c553f0d276b389b2b424e483304",
        "benchmark": BASE_DIR / "benchmarks" / "strix.json",
    }
]
