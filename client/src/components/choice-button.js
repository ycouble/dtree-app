import React from "react";
import classnames from "classnames";
import { Link } from "react-router-dom";

import css from "./css/choice-button.module.css";

const ChoiceButton = ({
  id,
  title,
  children_id,
  description,
  disabled,
  setSelected,
}) => {
  const choice = classnames(css.choice, { [css.disabledLink]: disabled });

  return description ? (
    <div className={choice} onClick={() => setSelected(id)}>
      {title}
    </div>
  ) : (
    <Link className={choice} to={`/dtree/${children_id}`} disabled={true}>
      {title}
    </Link>
  );
};

export default ChoiceButton;
