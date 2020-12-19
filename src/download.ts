
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

async function run() {
  const data = await restClient.get<IBroadcastDay[]>("broadcasts");
  if (data.result === null) {
    throw new Error("Got empty result");
  }
  data.result.forEach((day) => {
    day.broadcasts.forEach(async (broadcast) => {
      const subscription = config.subscriptions.find((s) => s.title === broadcast.title);
      if (subscription) {
        const detail = await restClient.get<IBroadcastDetail>(`broadcast/${broadcast.programKey}/${broadcast.broadcastDay}`);
        if (detail.result === null) {
          throw new Error("Got empty result");
        }
        process(new BroadcastDownloadTask(config, subscription, broadcast, detail.result.streams));
      }
    });
  });
}

run();
