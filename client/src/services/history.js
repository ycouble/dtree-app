import { getNodeById } from "./dtree";

export const getLastAnswer = (dtree, history) => {
  return history.reduce((acc, cValue) => {
    const node = getNodeById(dtree, cValue);
    if (node.type === "ANSWER") return node.title;
    else return acc;
  }, undefined);
};
