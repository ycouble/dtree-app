import React from "react";

import Button from "./button";
import StyledText from "./styled-text";
import css from "./css/step-vue.module.css";

const StepVue = ({ description, attachements, children, setNextNode }) => {
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
          <Button onClick={() => setNextNode(children[0].id)} text={"Suite"} />
        )}
      </div>
    </div>
  );
};

export default StepVue;
