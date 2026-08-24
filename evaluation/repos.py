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


    },

  {   "name": "click",
      "url": "https://github.com/pallets/click.git",
      "commit": "2c8cd3ac958a7eb316d67f2d316c27086c4c0369",
      "benchmark": BASE_DIR / "benchmarks" / "click.json",


    }
]
