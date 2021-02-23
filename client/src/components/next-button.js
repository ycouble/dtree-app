import React from "react";
import { Link } from "react-router-dom";

import Button from "./button";

import css from "./css/next-button.module.css";

const NextButton = ({ to, text = "Suite" }) => {
  return (
    <Link to={to} className={css.next}>
      <Button text={text} />
    </Link>
  );
};

export default NextButton;
