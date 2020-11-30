import React from "react";

import css from "./css/button.module.css";

const Button = ({ text, onClick }) => {
  return (
    <div className={css.button} onClick={onClick}>
      <span className={css.text}>{text}</span>
    </div>
  );
};

export default Button;
