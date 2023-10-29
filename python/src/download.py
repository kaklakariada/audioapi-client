import itertools
import json
from pathlib import Path
import sys
from typing import Iterable, NamedTuple

import requests

from api import get_download_tasks

sys.path.append(str(Path(__file__).parent.parent))
import config

def main():
    for t in get_download_tasks(config.baseUrl, config.subscriptions):
        print(f"Task: {t}")
    

if __name__ == "__main__":
    main()
