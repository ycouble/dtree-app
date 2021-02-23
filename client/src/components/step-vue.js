import React from "react";

import NextButton from "./next-button";
import css from "./css/step-vue.module.css";

const StepVue = ({ description, attachements, children }) => {
  return (
    <div>
      <div className={css.paragraphe}>
        {description.map(({ attributes, insert }, key) => {
          return (
            <div key={key} className={css.text}>
              {insert}
            </div>
          );
        })}
      </div>
      <div>
        {attachements?.map(({ id, title, href }) => {
          return <div key={id}>{title + " -> " + href}</div>;
        })}
        {children.length !== 0 && (
          <NextButton to={`/dtree/${children[0].id}`} />
        )}
      </div>
    </div>
  );
};

export default StepVue;
