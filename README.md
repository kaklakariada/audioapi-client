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

### Initial Setup

Create a config file with your subscriptions:

```py
base_folder = "/tmp/downloads"
base_url = "<audio api baseUrl>"
stream_base_url = "<stream base url>"
subscriptions = [
    {"title": "<title1>", "targetFolder": f"{base_folder}/path1"},
    {"title": "<title2>", "targetFolder": f"{base_folder}/path2"}
]
```

### Run

```sh
poetry run download
```

### Run Type & Style Checker

```sh
poetry run nox -s check
```

### Run Formatter

```sh
poetry run nox -s fix
```
