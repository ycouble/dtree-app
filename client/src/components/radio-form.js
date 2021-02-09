import React, { useState } from "react";
import "../services/capitalize";

// import classnames from "classnames";
import css from "./css/radio-form.module.css";

import Button from "./button";
import Icon from "./icon";

const RadioForm = ({ question, description, choices, next }) => {
  const [selected, setSelected] = useState();

  const onSelection = (id) => {
    setSelected(id);
  };

  const onNext = () => {
    if (selected) next(selected);
  };

  const descriptions = description.split("\n");

  return (
    <div className={css.form}>
      <div>
        <h2>{question.capitalize()}</h2>
        {descriptions.map((text, index) => {
          return <p key={index}>{text.capitalize()}</p>;
        })}
      </div>
      <div>
        {choices.map(({ labels, id }, index) => {
          const isSelected = id === selected;
          const iconName = isSelected
            ? "icons/radio-selected.svg"
            : "icons/radio.svg";

          return (
            <div
              className={css.choice}
              onClick={() => onSelection(id)}
              key={index}
            >
              <Icon path={iconName} />
              <div>{labels.toString()}</div>
            </div>
          );
        })}
      </div>
      <Button text="Suivant" onClick={() => onNext()} />
    </div>
  );
};

export default RadioForm;
