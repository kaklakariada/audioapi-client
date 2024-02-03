from pathlib import Path
from audioapi_client.api import DownloadTask, Subscription


def test_download_task_local_file():
    subscription = Subscription(title="title", programKey="progKey", broadcastDay="day", station="station", targetFolder=Path("path"))
    task = DownloadTask(subscription=subscription, streamId="stream", url="url", size=5)
    assert Path("path/stream") == task.local_path
