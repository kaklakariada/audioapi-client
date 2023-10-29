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

### Run Type Checker

```sh
poetry run mypy .
```

### Run Style Checker

```sh
poetry run pycodestyle *.py
```

### Run Formatter

```sh
poetry run autopep8 --in-place --aggressive *.py
```
