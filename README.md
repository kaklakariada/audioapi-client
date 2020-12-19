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
            { title: "<title1>", targetFolder: "<target path1>"},
            { title: "<title2>", targetFolder: "<target path2>"},
        ],
    };
    ```

1. Run `npm start` to generate `wget` commands for downloading the files.

## Development

Run linter: `npm run lint`
