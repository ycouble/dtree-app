import React from "react";
import classnames from "classnames";

import css from "./css/choice-button.module.css";

const ChoiceButton = ({
  id,
  title,
  children_id,
  description,
  disabled,
  setSelected,
  setNextNode,
}) => {
  const choice = classnames(css.choice, { [css.disabledLink]: disabled });

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
