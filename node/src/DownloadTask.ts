import { BroadcastSubscription, IBroadcast, IDownloadConfig, IStream } from "./lib";
import { StreamDownloadTask } from "./StreamDownloadTask";
export class BroadcastDownloadTask {
    constructor(
        readonly config: IDownloadConfig,
        readonly subscription: BroadcastSubscription,
        readonly broadcast: IBroadcast,
        readonly streams: IStream[]) { }

    public getStreams(): StreamDownloadTask[] {
        return this.streams.map((stream) => new StreamDownloadTask(this, stream));
    }
}
