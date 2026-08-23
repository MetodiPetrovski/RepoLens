from pathlib import Path

BASE_DIR = Path(__file__).parent



REPOSITORIES = [
    
  {
        "name": "strix",
        "url": "https://github.com/usestrix/strix.git",
        "commit": "f528a6d26585b05bd55909394a8186fb851fc39a ",
        "benchmark": BASE_DIR / "benchmarks" / "strix.json",
    }
]
