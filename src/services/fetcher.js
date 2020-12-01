import fetch from "isomorphic-unfetch";

const defaultContentType = {
  "Content-Type": "application/json; charset=utf-8",
};

const buildQueryStringForObject = (key, object) => {
  return Object.entries(object)
    .filter(([k, v]) => v !== undefined)
    .map(([k, v]) => `${key}[${k}]=${encodeURIComponent(v)}`)
    .join("&");
};

const buildQueryString = (params) => {
  return Object.keys(params)
    .filter((k) => !!params[k])
    .map((k) =>
      typeof params[k] === "object"
        ? buildQueryStringForObject(k, params[k])
        : `${k}=${encodeURIComponent(params[k])}`
    )
    .join("&");
};

export const fetcher = (method) => async (
  _url,
  body,
  params = {},
  _headers = {}
) => {
  const headers = { ...defaultContentType, ..._headers };

  // eslint-disable-next-line no-useless-catch
  try {
    const qs = buildQueryString(params);
    const url = qs.length === 0 ? _url : `${_url}?${qs}`;

    const reqOpts = {
      method: method || "POST",
      headers,
      body:
        method !== "GET" && body !== undefined
          ? JSON.stringify(body)
          : undefined,
    };
    const response = await fetch(url, reqOpts);

    if (response.ok && response.status === 204) return undefined;

    const resJSON = await response.json();
    if (response.ok === false) return Promise.reject(resJSON.error);
    return resJSON;
  } catch (err) {
    throw err;
  }
};

export const get = (url, params, headers) =>
  fetcher("GET")(url, undefined, params, headers);
export const post = fetcher("POST");
