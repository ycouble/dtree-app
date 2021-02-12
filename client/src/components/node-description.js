import React from "react";

import css from "./css/node-description.module.css";

const NodeDescription = ({ text }) => {
  return (
    <div className={css.paragraphe}>
      {text.split("\n").map((i, key) => {
        return (
          <p key={key} className={css.text}>
            {i}
          </p>
        );
      })}
    </div>
  );
};

export default NodeDescription;
