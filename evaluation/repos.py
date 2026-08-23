from pathlib import Path

BASE_DIR = Path(__file__).parent



REPOSITORIES = [
    
  {
        "name": "strix",
        "url": "https://github.com/usestrix/strix.git",
        "commit": "1c499c5b2d788c553f0d276b389b2b424e483304",
        "benchmark": BASE_DIR / "benchmarks" / "strix.json",
    },

  {   "name": "requests",
      "url": "https://github.com/psf/requests.git",
      "commit": "8f8b212de8c2129d7954c6cd373762880375620a",
      "benchmark": BASE_DIR / "benchmarks" / "requests.json",


    }
]
