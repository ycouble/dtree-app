import { get } from "./fetcher";
import { withConfiguration, getConfig } from "./config";

const api = "dtree-api";
const front = "dtree-front";

export const login_url = getConfig()[front] + "/login";
export const redirect_url = getConfig()[front] + "/redirect";

export const getNode = async (body) => {
  return withConfiguration(async (config) => {
    const endpoint = `${config[api]}/api/dtree`;
    return get(endpoint, body);
  });
};

export const login = async (body) => {
  return withConfiguration(async (config) => {
    const endpoint = `${config[api]}/api/user/login`;
    return get(endpoint, body, true);
  });
};

export const connected = async (body) => {
  return withConfiguration(async (config) => {
    const endpoint = `${config[api]}/api/user/connected`;
    return get(endpoint, body, true);
  });
};

export const redirect = async (body) => {
  return withConfiguration(async (config) => {
    const endpoint = `${config[api]}/api/user/redirect`;
    return get(endpoint, body, true);
  });
};

export const logout = async (body) => {
  return withConfiguration(async (config) => {
    const endpoint = `${config[api]}/api/user/logout`;
    return get(endpoint, body, true);
  });
};