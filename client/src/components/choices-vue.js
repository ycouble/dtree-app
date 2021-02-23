import React from "react";

import ChoiceButton from "./choice-button";
import css from "./css/choices-vue.module.css";

const ChoicesVue = ({ question, children }) => {
  return (
    <div>
      {question && <h3>{question}</h3>}
      <div className={css.choices}>
        {children.map((child, index) => {
          return <ChoiceButton key={index} {...child} />;
        })}
      </div>
    </div>
  );
};

export default ChoicesVue;
