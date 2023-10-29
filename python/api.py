import itertools
from pathlib import Path
from typing import Iterable, NamedTuple

import requests

class Subscription(NamedTuple):
    title: str
    targetFolder: Path
    programKey: str
    broadcastDay: str
    station: str


class DownloadTask(NamedTuple):
    subscription: Subscription
    streamId: str


def get_broadcasts(base_url: str) -> dict:
    url = f"{base_url}/broadcasts"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


def get_subscriptions(broadcast_data: dict, subscriptions: list[dict[str, str]]) -> Iterable[Subscription]:
    subscription_target_folders: dict[str, Path] = {subscription["title"]: Path(
        subscription["targetFolder"]) for subscription in subscriptions}
    broadcasts_per_day = (day["broadcasts"] for day in broadcast_data)
    broadcasts = itertools.chain.from_iterable(broadcasts_per_day)
    subscribed_broadcasts = (
        b for b in broadcasts if b["title"] in subscription_target_folders)
    return (Subscription(title=b["title"],
                         station=b["station"],
                         targetFolder=subscription_target_folders[b["title"]],
                         broadcastDay=b["broadcastDay"],
                         programKey=b["programKey"]) for b in subscribed_broadcasts)


def get_broadcast_detail(base_url: str, task: Subscription) -> dict:
    r = requests.get(
        f"{base_url}/broadcast/{task.programKey}/{task.broadcastDay}")
    r.raise_for_status()
    return r.json()


def get_streams(base_url: str, task: Subscription) -> Iterable[DownloadTask]:
    detail = get_broadcast_detail(base_url, task)
    return (DownloadTask(streamId=stream["loopStreamId"], subscription=task) for stream in detail["streams"])


def get_download_tasks(base_url: str, subscriptions: list[dict[str, str]]) -> Iterable[DownloadTask]:
    broadcasts = get_broadcasts(base_url)
    tasks = (get_streams(base_url, task)
             for task in get_subscriptions(broadcasts, subscriptions))
    return itertools.chain.from_iterable(tasks)
