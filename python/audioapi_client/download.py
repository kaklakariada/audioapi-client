import os
from concurrent import futures
from pathlib import Path
from typing import Iterable

import requests
import tqdm

from audioapi_client.api import DownloadTask


def download_one(task: DownloadTask) -> None:
    target_file = task.subscription.targetFolder / task.streamId
    if not target_file.parent.is_dir():
        os.makedirs(target_file.parent)
    return start_download(target_file, task.url)


def start_download(target_file: Path, url: str) -> None:
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size_in_bytes = int(r.headers.get("content-length", 0))
        print(f"remote size: {total_size_in_bytes}, status: {r.status_code}")
        block_size = 1024  # 1 Kibibyte
        progress_bar = tqdm.tqdm(total=total_size_in_bytes, unit="iB", unit_scale=True)
        with open(target_file, "wb") as file:
            for data in r.iter_content(block_size):
                file.write(data)
                progress_bar.update(len(data))
        progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        raise AssertionError(f"Expected {total_size_in_bytes} bytes but got {progress_bar.n}")


def download(tasks: list[DownloadTask]) -> None:
    print(f"Starting {len(tasks)} downloads...")
    with futures.ThreadPoolExecutor(max_workers=4) as executor:
        result = executor.map(download_one, tasks)
    for r in result:
        print(f"Task finished: {r}")
    print("Done")
