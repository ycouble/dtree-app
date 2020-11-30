import React, { useState } from "react";

import spec from "./data/spec.json";
import css from "./app.module.css";

import RadioForm from "./components/radio-form";
import NumberInput from "./components/number-input";

function App() {
  const [form, setForm] = useState(1);

  console.log(spec["localisation"]);
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
    </div>
  );
}

export default App;
