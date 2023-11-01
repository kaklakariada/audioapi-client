from pathlib import Path
import sys

import config
from api import get_download_tasks
from download import download


def main() -> None:
    tasks = get_download_tasks(config.base_url,config.stream_base_url, config.subscriptions)
    download(list(tasks))


if __name__ == "__main__":
    main()
