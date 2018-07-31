# audioapi-client
Client for audioapi

## Usage

1. Run `npm install`
1. Create file `config.ts` in the project folder with the following content:

    ```typescript
    import { BroadcastSubscription, IDownloadConfig } from "./src/lib";
    
    export const config: IDownloadConfig = {
        baseUrl: "<audio api baseUrl>",
        streamBaseUrl: "<stream base url>",
        subscriptions: [
            new BroadcastSubscription("<title1>", "<target path1>"),
            new BroadcastSubscription("<title2>", "<target path2>")
        ],
    };
    ```

1. Run `npm start` to generate `wget` commands for downloading the files.

## Development

Run linter: `npm run lint`
