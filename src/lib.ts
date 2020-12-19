
export interface IBroadcast {
    href: string;
    station: string;
    id: number;
    broadcastDay: number;
    programKey: string;
    title: string;
}

export interface IBroadcastDetail {
    href: string;
    station: string;
    id: number;
    broadcastDay: number;
    programKey: string;
    title: string;
    streams: IStream[];
}

export interface IStream {
    alias: string;
    loopStreamId: string;
}

export interface IBroadcastDay {
    day: number;
    broadcasts: IBroadcast[];
}

export interface BroadcastSubscription {
    title: string;
    targetFolder: string;
}

export interface IDownloadConfig {
    baseUrl: string;
    streamBaseUrl: string;
    subscriptions: BroadcastSubscription[];
}
