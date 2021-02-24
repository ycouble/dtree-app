import React, { useState, useEffect } from "react";

import StyledText from "./styled-text";
import ChoiceButton from "./choice-button";
import NextButton from "./next-button";
import css from "./css/choices-vue.module.css";

const ChoicesVue = ({ question, children }) => {
  const [selected, setSelected] = useState();

  const selectedChildren = children.find(({ id }) => id === selected);

  useEffect(() => {
    if (!selectedChildren) setSelected(undefined);
  }, [selectedChildren]);

  return (
    <div>
      {question && <h3>{question}</h3>}
      <div className={css.choices}>
        {children.map((child, index) => {
          return (
            <ChoiceButton
              key={index}
              {...child}
              disabled={!!selected}
              setSelected={setSelected}
            />
          );
        })}
      </div>
      {selectedChildren && (
        <div>
          <StyledText styledText={selectedChildren.description} />
          <NextButton to={`/dtree/${selectedChildren.children_id[0]}`} />
        </div>
      )}
    </div>
  );
};

export default ChoicesVue;
