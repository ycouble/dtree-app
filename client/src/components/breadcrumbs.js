import React from "react";

import { getNodeById } from "../services/dtree";
import { capitalize, getFirstWords } from "../services/string-functions";
import css from "./css/breadcrumbs.module.css";

const NodeLink = ({ title, isQuestion, onClick }) => {
  return (
    <div className={css.nodeLink}>
      <div className={css.link} onClick={onClick}>
        <span>{title}</span>
        {isQuestion && <span>{"... "}</span>}
      </div>
      <span>{">"}</span>
    </div>
  );
};

const Breadcrumbs = ({ dtree, history, setHistory }) => {
  const returnToNode = (id) => () => {
    const idx = history.indexOf(id);
    setHistory(history.slice(0, idx + 1));
  };

  return (
    <div className={css.breadcrumbs}>
      <NodeLink title={"Accueil"} onClick={returnToNode(history[0])} />
      {history.slice(0, -1).map((id) => {
        const node = getNodeById(dtree, id);
        if (node?.type !== "STEP" && node?.type !== "QUESTION") return;
        const isStep = node.type === "STEP";
        const title = isStep
          ? capitalize(node.title).slice(0, 8)
          : capitalize(getFirstWords(node.title));
        return (
          <NodeLink
            key={id}
            title={title}
            isQuestion={!isStep}
            onClick={returnToNode(id)}
          />
        );
      })}
    </div>
  );
};

export default Breadcrumbs;
