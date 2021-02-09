import React from "react";

import css from "./css/button.module.css";

const Button = ({ text, onClick }) => {
  return (
    <div className={css.button} onClick={onClick}>
      {text.split("\n").map((i, key) => {
        return (
          <div key={key} className={css.text}>
            {i}
          </div>
        );
      })}
    </div>
  );
};

export default Button;
