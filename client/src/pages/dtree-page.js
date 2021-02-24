import React from "react";

import { Breadcrumbs, ChoicesVue, StepVue } from "../components";
import useLocalStorage from "../hooks/useLocalStorage";
import { getRootNode, getFormattedNode } from "../services/dtree";
import { getLastAnswer } from "../services/history";

import css from "./css/dtree-page.module.css";

const DtreePage = ({ dtree }) => {
  const startNode = getRootNode(dtree).children_id[0];
  const [history, setHistory] = useLocalStorage("history", [startNode]);

  const currentNodeId = history[history.length - 1];

  const setNextNode = (nextNodeId, nodeId) => {
    const historyToAdd = nodeId ? [nodeId, nextNodeId] : [nextNodeId];
    setHistory([...history, ...historyToAdd]);
  };

  const node = getFormattedNode(dtree, currentNodeId);
  const lastAnswer = getLastAnswer(dtree, history);
  return (
    <div className={css.page}>
      <Breadcrumbs dtree={dtree} history={history} setHistory={setHistory} />
      {lastAnswer && <div className={css.lastAnswer}>{lastAnswer}</div>}
      <h2>{node.title}</h2>
      {node.type === "STEP" ? (
        <StepVue {...node} setNextNode={setNextNode} />
      ) : (
        <ChoicesVue {...node} setNextNode={setNextNode} />
      )}
    </div>
  );
};

export default DtreePage;
