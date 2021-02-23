import React from "react";
import { Redirect, Link } from "react-router-dom";
import { useParams } from "react-router-dom";

import { NodeDescription } from "../components";
import css from "./css/home-page.module.css";

import {
  getNodeById,
  getChildrenID,
  getFormattedNode,
} from "../services/dtree";

const HomePage = ({ dtree }) => {
  const { id } = useParams();
  if (getNodeById(dtree, id) === undefined)
    return <Redirect to={`/dtree/${getChildrenID(dtree)}`} />;

  const node = getFormattedNode(dtree, id);
  return (
    <div className={css.page}>
      {node && (
        <div>
          {node.step_title && <h2>{node.step_title}</h2>}
          <h2>{node.title}</h2>
          {node.description ? (
            <div>
              <NodeDescription text={node.description} />
              <div>
                {node.attachements?.map(({ id, title, href }) => {
                  return <div key={id}>{title + " -> " + href}</div>;
                })}
                {node.children.length !== 0 && (
                  <Link
                    className={css.choice}
                    to={`/dtree/${node.children_id[0]}`}
                  >
                    Suivant
                  </Link>
                )}
              </div>
            </div>
          ) : (
            <div className={css.buttonSet}>
              {node.children.map(({ id, title, children_id }) => {
                return (
                  <Link
                    className={css.choice}
                    key={id}
                    to={`/dtree/${children_id}`}
                  >
                    {title}
                  </Link>
                );
              })}
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default HomePage;
