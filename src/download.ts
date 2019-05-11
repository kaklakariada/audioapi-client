
import * as rm from "typed-rest-client/RestClient";
import { config } from "../config";
import { BroadcastDownloadTask } from "./DownloadTask";
import { IBroadcastDay, IBroadcastDetail } from "./lib";
const restClient: rm.RestClient = new rm.RestClient("audioapi-client", config.baseUrl);

function process(task: BroadcastDownloadTask): void {
  task.getStreams().forEach((streamDownload) => {
    console.log(streamDownload.getWgetCommand());
  });
}

function run() {
  restClient.get<IBroadcastDay[]>("broadcasts")
    .then((data) => {
      if (data.result === null) {
        throw new Error("Got empty result");
      }
      data.result.forEach((day) => {
        day.broadcasts.forEach((broadcast) => {
          const subscription = config.subscriptions.find((s) => s.matches(broadcast));
          if (subscription) {
            restClient.get<IBroadcastDetail>(`broadcast/${broadcast.programKey}/${broadcast.broadcastDay}`)
              .then((detail) => {
                if (detail.result === null) {
                  throw new Error("Got empty result");
                }
                process(new BroadcastDownloadTask(config, subscription, broadcast, detail.result.streams));
              });
          }
        });
      });
    })
    .catch((reason) => console.error("Failure: ", reason));
}

run();
