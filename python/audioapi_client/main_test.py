
from pathlib import Path
from audioapi_client.api import DownloadTask, Subscription
from audioapi_client.main import already_exists
import pytest


@pytest.fixture
def subscription(tmp_path):
    return Subscription(title="title", programKey="progKey", broadcastDay="day", station="station", targetFolder=tmp_path)


def test_already_exists_no_file(tmp_path: Path, subscription: Subscription):
    assert not already_exists(DownloadTask(subscription=subscription, streamId="stream", url="url", size=5))


def test_already_exists_empty_file(tmp_path: Path, subscription: Subscription):
    file = tmp_path / "stream"
    file.write_text("")
    assert not already_exists(DownloadTask(subscription=subscription, streamId="stream", url="url", size=5))

def test_already_exists_non_empty(tmp_path: Path, subscription: Subscription):
    file = tmp_path / "stream"
    file.write_text("123")
    assert not already_exists(DownloadTask(subscription=subscription, streamId="stream", url="url", size=5))

def test_already_exists_one_byte_missing(tmp_path: Path, subscription: Subscription):
    file = tmp_path / "stream"
    file.write_text("1234")
    assert already_exists(DownloadTask(subscription=subscription, streamId="stream", url="url", size=5))

def test_already_exists_expected_size(tmp_path: Path, subscription: Subscription):
    file = tmp_path / "stream"
    file.write_text("12345")
    assert already_exists(DownloadTask(subscription=subscription, streamId="stream", url="url", size=5))

def test_already_exists_too_large(tmp_path: Path, subscription: Subscription):
    file = tmp_path / "stream"
    file.write_text("123456")
    assert not already_exists(DownloadTask(subscription=subscription, streamId="stream", url="url", size=5))
