# audioapi-client
Clients for audioapi

## Node.js client

### Usage

1. Run `npm install`
1. Create file `config.ts` in the project folder with the following content:

    ```typescript
    import { IDownloadConfig } from "./src/lib";
    
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

### Development

Run linter: `npm run lint`


## Python client

### Run

```sh
poetry run download 
```

### Run Type Checker

```sh
poetry run mypy audioapi_client/
```

### Run Style Checker

```sh
poetry run black audioapi_client/ --check
```

### Run Formatter

```sh
poetry run black audioapi_client/
```
