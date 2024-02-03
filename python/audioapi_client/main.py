import sys
from pathlib import Path

import audioapi_client.config
from audioapi_client.api import get_download_tasks, DownloadTask
from audioapi_client.config import base_folder, base_url, stream_base_url, subscriptions
from audioapi_client.download import download

def already_exists(task: DownloadTask) -> bool:
    target_file = task.local_path
    if not target_file.is_file():
        print(f"Local file {target_file} does not exist")
        return False
    local_size = target_file.stat().st_size
    if local_size == task.size:
        print(f"Local file {target_file} has expected size, nothing to do")
        return True
    if local_size == task.size - 1:
        print(f"Local file {target_file} has expected size minus one && , nothing to do")
        return True
    return False

def main() -> None:
    tasks = get_download_tasks(base_url, stream_base_url, subscriptions)
    tasks = (t for t in tasks if not already_exists(t))
    download(list(tasks))


if __name__ == "__main__":
    main()
