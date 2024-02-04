import argparse
import sys
from pathlib import Path

import audioapi_client.config
from audioapi_client.api import DownloadTask, get_download_tasks
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

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION]...",
        description="Download subscriptions using the Audio API"
    )
    parser.add_argument(
        "-d", "--dry-run", action='store_true', help="Dry run: only check if new files are available but does not download them."
    )
    return parser

def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    tasks = get_download_tasks(base_url, stream_base_url, subscriptions)
    tasks = [t for t in tasks if not already_exists(t)]
    if args.dry_run:
        print(f"Dry run: skip download of {len(tasks)} files.")
    else:
        print(f"Starting {len(tasks)} downloads...")
        download(tasks)
        print("Done")


if __name__ == "__main__":
    main()
