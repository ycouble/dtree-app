import axios from "axios";

export const get = async (url, body, withCredentials = false) => {
  try {
    const response = await axios.get(url, {
      withCredentials,
      params: body,
    });
    return response.data;
  } catch (error) {
    console.log("error", error);
  }
};

export const post = async (url, body, withCredentials = false) => {
  try {
    const response = await axios.post(url, body, { withCredentials });
    return response.data;
  } catch (error) {
    console.log("error", error);
  }
};
