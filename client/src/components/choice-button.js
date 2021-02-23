import React from "react";
import { Link } from "react-router-dom";

import css from "./css/choice-button.module.css";

const ChoiceButton = ({ title, children_id }) => {
  return (
    <Link className={css.choice} to={`/dtree/${children_id}`}>
      {title}
    </Link>
  );
};

export default ChoiceButton;
