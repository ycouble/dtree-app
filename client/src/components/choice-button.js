import React from "react";
import classnames from "classnames";

import css from "./css/choice-button.module.css";

const ChoiceButton = ({
  id,
  title,
  children_id,
  description,
  selected,
  setSelected,
  setNextNode,
}) => {
  const choice = classnames(
    css.choice,
    { [css.disabledLink]: !!selected },
    { [css.selected]: id === selected },
    { [css.disabled]: id !== selected && !!selected }
  );

  return description ? (
    <div className={choice} onClick={() => setSelected(id)}>
      {title}
    </div>
  ) : (
    <div className={choice} onClick={() => setNextNode(children_id[0], id)}>
      {title}
    </div>
  );
};

export default ChoiceButton;
