
export interface IBroadcast {
    href: string;
    station: string;
    id: number;
    broadcastDay: number;
    programKey: string;
    title: string;
}

export interface IBroadcastDay {
    day: number;
    broadcasts: IBroadcast[];
}

export class BroadcastSubscription {
    constructor(
        public readonly title: string,
        readonly targetFolder: string) { }
    public matches(broadcast: IBroadcast): boolean {
        return this.title === broadcast.title;
    }
}

export interface IDownloadConfig {
    baseUrl: string;
    subscriptions: BroadcastSubscription[];
}

export interface IDownloadTask {
    readonly subscription: BroadcastSubscription;
    readonly broadcast: IBroadcast;
}
