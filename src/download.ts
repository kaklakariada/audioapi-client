
import * as rm from "typed-rest-client/RestClient";
import { config } from "../config";
import { IBroadcast, IBroadcastDay, IBroadcastDetail, IDownloadTask } from "./lib";
const restClient: rm.RestClient = new rm.RestClient("audioapi-client", config.baseUrl);

function process(task: IDownloadTask): void {
  task.streams.forEach((stream) => {
    const streamUrl = `${config.streamBaseUrl}?channel=${task.broadcast.station}&id=${stream.loopStreamId}`;
    console.log(streamUrl);
  });
}

function run() {
    restClient.get<IBroadcastDay[]>("broadcasts")
      .then((data) => {
        if(data.result === null) {
          throw new Error("Got empty result");
        }
        data.result.forEach((day) => {
          day.broadcasts.forEach((b) => {
            const sub = config.subscriptions.find((s) => s.matches(b));
            if (sub) {
              restClient.get<IBroadcastDetail>(`broadcast/${b.programKey}/${b.broadcastDay}`)
                .then((detail) => {
                  if (detail.result === null) {
                    throw new Error("Got empty result");
                  }
                  console.log(detail);
                  process({ subscription: sub, broadcast: b, streams: detail.result.streams });
              });
            }
          });
        });
      })
      .catch((reason) => console.error("Failure: ", reason));
}

run();
