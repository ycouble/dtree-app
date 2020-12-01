import React, { useState, useEffect } from "react";

import spec from "./data/spec.json";
import css from "./app.module.css";

import BooleanChoice from "./components/boolean-choice";
import NumberInput from "./components/number-input";
import RadioForm from "./components/radio-form";

import { getNode } from "./services/api";

function App() {
  const [form, setForm] = useState();
  const [nodeId, setId] = useState();

  useEffect(() => {
    const getData = async () => {
      const body = {
        id: nodeId,
      };
      const results = await getNode(body);

      setForm(results);
    };

    getData();
  }, [nodeId]);

  return (
    <div className={css.app}>
      <header className={css.header}>
        <h1>Decision Tree Webapp</h1>
      </header>
      {form && <RadioForm {...form} next={setId} />}
    </div>
  );
}

export default App;
