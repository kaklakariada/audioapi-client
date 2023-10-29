from concurrent import futures
from typing import Iterable

from api import DownloadTask

def download_one(task: DownloadTask) -> None:
    print("Download", task)


def download(tasks: list[DownloadTask]) -> None:
    print(f"Starting {len(tasks)} downloads...")
    with futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(download_one, tasks)
    print("Done")