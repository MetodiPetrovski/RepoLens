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
      "commit": "d38495c90653496c3c81f31e8f9bef162b400b44",
      "benchmark": BASE_DIR / "benchmarks" / "requests.json",


    }
]
