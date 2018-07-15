import { BroadcastDownloadTask } from "./DownloadTask";
import { BroadcastSubscription, IBroadcast, IDownloadConfig, IStream } from "./lib";

export class StreamDownloadTask {
    constructor(
        readonly downloadTask: BroadcastDownloadTask,
        readonly stream: IStream,
    ) { }

    public getWgetCommand(): string {
        return `wget "${this.getDownloadUrl()}" -O ${this.getTargetFile()}`;
    }

    public getDownloadUrl(): string {
        return `${this.getStreamBaseUrl()}?channel=${this.getStation()}&id=${this.getStreamId()}`;
    }

    public getTargetFile(): string {
        return `${this.getTargetFolder()}/${this.getStreamId()}`;
    }

    private getTargetFolder() {
        return this.downloadTask.subscription.targetFolder;
    }

    private getStation() {
        return this.downloadTask.broadcast.station;
    }

    private getStreamBaseUrl() {
        return this.downloadTask.config.streamBaseUrl;
    }

    private getStreamId(): string {
        return this.stream.loopStreamId;
    }
}