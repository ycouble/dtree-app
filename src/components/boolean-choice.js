import React, { useState } from "react";
import "../services/capitalize";

// import classnames from "classnames";
import css from "./css/boolean-choice.module.css";

import Button from "./button";

const BooleanChoice = ({ question, description, reponses, next }) => {
  const [selected, setSelected] = useState();

  const onSelection = (dest) => (e) => {};

  const onNext = (choice) => (e) => {
    console.log(choice + " is selected.");
    next();
  };

  return (
    <div className={css.form}>
      <div>
        <h2>{question.capitalize()}</h2>
        <p>{description.capitalize()}</p>
      </div>
      <Button text="Oui" onClick={onNext(true)} />
      <Button text="Non" onClick={onNext(false)} />
    </div>
  );
};

export default BooleanChoice;
