import React, { useState } from "react";

import spec from "./data/spec.json";
import css from "./app.module.css";

import BooleanChoice from "./components/boolean-choice";
import NumberInput from "./components/number-input";
import RadioForm from "./components/radio-form";

function App() {
  const [form, setForm] = useState(0);

  const nextForm = () => {
    setForm(form + 1);
  };

  return (
    <div className={css.app}>
      <header className={css.header}>
        <h1>Decision Tree Webapp</h1>
      </header>
      {form === 0 && <RadioForm {...spec["localisation"]} next={nextForm} />}
      {form === 1 && (
        <NumberInput
          {...spec["localisation"]["branches"]["entrepot"]}
          next={nextForm}
        />
      )}
      {form === 2 && (
        <BooleanChoice
          {...spec["localisation"]["branches"]["produit"]}
          next={nextForm}
        />
      )}
    </div>
  );
}

export default App;
