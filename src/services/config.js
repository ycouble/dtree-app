import config from "../config.json";

export const withConfiguration = (cb) => cb(config[process.env.REACT_APP_ENV]);

export const getConfig = () => config[process.env.REACT_APP_ENV];
