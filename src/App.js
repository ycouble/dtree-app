import React from "react";

import spec from "./data/spec.json";
import css from "./app.module.css";

import RadioForm from "./components/radio-form";

function App() {
  console.log(spec["localisation"]);
  return (
    <div className={css.app}>
      <header className={css.header}>
        <h1>Decision Tree Webapp</h1>
      </header>
      <RadioForm {...spec["localisation"]} />
    </div>
  );
}

export default App;
