from pathlib import Path
import sys

import config
from api import get_download_tasks

def main():
    for t in get_download_tasks(config.base_url, config.subscriptions):
        print(f"Task: {t}")
   
if __name__ == "__main__":
    main()
