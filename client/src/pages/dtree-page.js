import React from "react";
import { Redirect, useParams } from "react-router-dom";

import { ChoicesVue, StepVue } from "../components";
import css from "./css/dtree-page.module.css";

import {
  getNodeById,
  getChildrenID,
  getFormattedNode,
} from "../services/dtree";

const DtreePage = ({ dtree }) => {
  const { id } = useParams();
  if (getNodeById(dtree, id) === undefined)
    return <Redirect to={`/dtree/${getChildrenID(dtree)}`} />;

  const node = getFormattedNode(dtree, id);
  return (
    <div className={css.page}>
      <h2>{node.title}</h2>
      {node.type === "STEP" ? <StepVue {...node} /> : <ChoicesVue {...node} />}
    </div>
  );
};

export default DtreePage;
