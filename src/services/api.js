import { get } from "./fetcher";
import { withConfiguration } from "./config";

export const getNode = async (body) => {
  return withConfiguration(async (config) => {
    const endpoint = `${config}/api/v1/dtree`;
    return get(endpoint, body);
  });
};
