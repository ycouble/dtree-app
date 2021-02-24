import React, { useState, useEffect } from "react";

import Button from "./button";
import StyledText from "./styled-text";
import ChoiceButton from "./choice-button";
import css from "./css/choices-vue.module.css";

const ChoicesVue = ({ question, children, setNextNode }) => {
  const [selected, setSelected] = useState();

  const selectedChildren = children.find(({ id }) => id === selected);

  useEffect(() => {
    if (!selectedChildren) setSelected(undefined);
  }, [selectedChildren]);

  return (
    <div>
      {question && <h3>{question}</h3>}
      <div className={css.choices}>
        {children.map((child) => {
          return (
            <ChoiceButton
              key={child.id}
              {...child}
              disabled={!!selected}
              setSelected={setSelected}
              setNextNode={setNextNode}
            />
          );
        })}
      </div>
      {selectedChildren && (
        <div>
          <StyledText styledText={selectedChildren.description} />
          <Button
            onClick={() =>
              setNextNode(selectedChildren.children_id[0], selectedChildren.id)
            }
            text={"Suite"}
          />
        </div>
      )}
    </div>
  );
};

export default ChoicesVue;
