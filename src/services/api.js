import { get } from "./fetcher";
import { withConfiguration } from "./config";

export const getNode = async (body) => {
  return withConfiguration(async (config) => {
    const endpoint = `${config}/api/dtree`;
    return get(endpoint, body);
  });
};

export const login = async (body) => {
  return withConfiguration(async (config) => {
    const endpoint = `${config}/api/login`;
    return get(endpoint, body, true);
  });
};

export const connected = async (body) => {
  return withConfiguration(async (config) => {
    const endpoint = `${config}/api/connected`;
    return get(endpoint, body, true);
  });
};

export const redirect = async (body) => {
  return withConfiguration(async (config) => {
    const endpoint = `${config}/api/redirect`;
    return get(endpoint, body, true);
  });
};

export const logout = async (body) => {
  return withConfiguration(async (config) => {
    const endpoint = `${config}/api/logout`;
    return get(endpoint, body, true);
  });
};
