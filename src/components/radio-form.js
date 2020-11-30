import React, { useState } from "react";
import "../services/capitalize";

// import classnames from "classnames";
import css from "./css/radio-form.module.css";

import Icon from "./icon";

const RadioForm = ({ question, description, reponses }) => {
  const [selected, setSelected] = useState();

  const onSelection = (dest) => (e) => {
    console.log(dest + " is selected.");
    setSelected(dest);
  };

  return (
    <div className={css.form}>
      <div>
        <h2>{question.capitalize()}</h2>
        <p>{description.capitalize()}</p>
      </div>
      <div>
        {reponses.map(({ nom, dest }, index) => {
          const isSelected = dest === selected;
          const iconName = isSelected
            ? "icons/radio-selected.svg"
            : "icons/radio.svg";

          return (
            <div className={css.choice} onClick={onSelection(dest)} key={index}>
              <Icon path={iconName} />
              <div>{nom}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default RadioForm;
