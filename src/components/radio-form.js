import React, { useState } from "react";
import "../services/capitalize";

// import classnames from "classnames";
import css from "./css/radio-form.module.css";

import Button from "./button";
import Icon from "./icon";

const RadioForm = ({ question, description, reponses, next }) => {
  const [selected, setSelected] = useState();

  const onSelection = (dest) => {
    console.log(dest + " is selected.");
    setSelected(dest);
  };

  const onNext = () => {
    if (selected) next();
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
            <div
              className={css.choice}
              onClick={() => onSelection(dest)}
              key={index}
            >
              <Icon path={iconName} />
              <div>{nom}</div>
            </div>
          );
        })}
      </div>
      <Button text="Suivant" onClick={() => onNext()} />
    </div>
  );
};

export default RadioForm;
