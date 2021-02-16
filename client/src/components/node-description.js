import React from "react";

import css from "./css/node-description.module.css";

const NodeDescription = ({ text }) => {
  return (
    <div className={css.paragraphe}>
      {text.map(({ attributes, insert }, key) => {
        return (
          <div key={key} className={css.text}>
            {insert.split("\n").map((i, key) => {
              return (
                <p key={key} className={css.text}>
                  {i}
                </p>
              );
            })}
          </div>
        );
      })}
    </div>
  );
};

export default NodeDescription;
