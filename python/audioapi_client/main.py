from pathlib import Path
import sys

import audioapi_client.config
from audioapi_client.api import get_download_tasks
from audioapi_client.download import download
from audioapi_client.config import base_folder, base_url, stream_base_url, subscriptions

def main() -> None:
    tasks = get_download_tasks(base_url,stream_base_url, subscriptions)
    download(list(tasks))


if __name__ == "__main__":
    main()
