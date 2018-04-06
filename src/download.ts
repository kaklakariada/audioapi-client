import {get} from "request-promise-native";
import {Observable} from "rxjs";
import {config} from "../config";
import {IBroadcastDay} from "./lib";

Observable.fromPromise(get(config.broadcastBaseUrl))
  .map((res: any) => JSON.parse(res))
  .flatMap((days: IBroadcastDay[]) => Observable.from(days))
  .flatMap((day) => Observable.from(day.broadcasts))
  .map((b) => {
    const sub = config.subscriptions.find((s) => s.matches(b));
    if(sub === undefined) {
      return undefined;
    }
    return {subscription: sub, broadcast: b};
  })
  .filter((task) => task !== undefined)
  .forEach((res) => console.log(res));
