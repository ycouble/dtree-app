import React, { useState } from "react";
import "../services/capitalize";

// import classnames from "classnames";
import css from "./css/number-input.module.css";

import Button from "./button";

const isBetween = (between, value) => {
  return between[0] <= value && (between[1] === -1 || between[1] > value);
};

const NumberInput = ({ question, description, unit, reponses, next }) => {
  const [value, setValue] = useState(0);

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  const onNext = (e) => {
    const inputValue = parseInt(value);
    if (!isNaN(inputValue) && inputValue >= 0) {
      const result = reponses.filter((response) =>
        isBetween(response.between, inputValue)
      );
      console.log(result);
      next();
    }
  };

  return (
    <div className={css.form}>
      <div>
        <h2>{question.capitalize()}</h2>
        <p>{description.capitalize()}</p>
      </div>
      <div className={css.input}>
        <input value={value} onChange={handleChange} />
        <div>{unit}</div>
      </div>
      <Button text="Suivant" onClick={onNext} />
    </div>
  );
};

export default NumberInput;
