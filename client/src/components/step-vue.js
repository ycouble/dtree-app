import React from "react";

import StyledText from "./styled-text";
import NextButton from "./next-button";
import css from "./css/step-vue.module.css";

const StepVue = ({ description, attachements, children }) => {
  return (
    <div>
      <div className={css.description}>
        <StyledText styledText={description} />
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
