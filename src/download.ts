
import * as rm from "typed-rest-client/RestClient";
import { config } from "../config";
import { IBroadcast, IBroadcastDay, IDownloadTask } from "./lib";
const restClient: rm.RestClient = new rm.RestClient("audioapi-client", config.baseUrl);

async function run() {
  try {
    const broadcastDays: rm.IRestResponse<IBroadcastDay[]> = await restClient.get<IBroadcastDay[]>("broadcasts");
    if (broadcastDays.result == null) {
      throw new Error("Got empty result");
    }
    const tasks: IDownloadTask[] = [];
    broadcastDays.result.forEach((day) =>
      day.broadcasts.forEach((b) => {
        const sub = config.subscriptions.find((s) => s.matches(b));
        if (sub) {
          tasks.push({ subscription: sub, broadcast: b });
        }
      }));
    console.log(tasks.length);

  } catch (err) {
    console.error("Failed: " + err.message);
  }
}

run();
