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
    url: str


def get_broadcasts(base_url: str) -> dict:
    url = f"{base_url}/broadcasts"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


def get_subscriptions(broadcast_data: dict,
                      subscriptions: list[dict[str, str]]) -> Iterable[Subscription]:
    subscription_target_folders: dict[str, Path] = {subscription["title"]: Path(
        subscription["targetFolder"]) for subscription in subscriptions}
    broadcasts_per_day = (day["broadcasts"] for day in broadcast_data)
    broadcasts = itertools.chain.from_iterable(broadcasts_per_day)
    subscribed_broadcasts = (
        b for b in broadcasts if b["title"] in subscription_target_folders)
    return (create_subscription(b, subscription_target_folders[b["title"]]) for b in subscribed_broadcasts)


def create_subscription(broadcast: dict, target_folder: Path) -> Subscription:
    return Subscription(title=broadcast["title"],
                        station=broadcast["station"],
                        targetFolder=target_folder,
                        broadcastDay=broadcast["broadcastDay"],
                        programKey=broadcast["programKey"])


def get_broadcast_detail(base_url: str, task: Subscription) -> dict:
    r = requests.get(
        f"{base_url}/broadcast/{task.programKey}/{task.broadcastDay}")
    r.raise_for_status()
    return r.json()


def get_streams(base_url: str, subscription: Subscription, stream_base_url: str) -> Iterable[DownloadTask]:
    detail = get_broadcast_detail(base_url, subscription)
    return (create_download_task(stream, subscription, stream_base_url) for stream in detail["streams"])


def create_download_task(stream: dict, subscription: Subscription, stream_base_url: str) -> DownloadTask:
    stream_id = stream["loopStreamId"]
    url = f"{stream_base_url}?channel={subscription.station}&id={stream_id}"
    return DownloadTask(streamId=stream_id, subscription=subscription, url=url)


def get_download_tasks(
        base_url: str, stream_base_url: str, subscriptions: list[dict[str, str]]) -> Iterable[DownloadTask]:
    broadcasts = get_broadcasts(base_url)
    tasks = (get_streams(base_url, task, stream_base_url)
             for task in get_subscriptions(broadcasts, subscriptions))
    return itertools.chain.from_iterable(tasks)
