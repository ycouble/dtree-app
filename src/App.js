import React, { useState, useEffect } from "react";

import spec from "./data/spec.json";
import css from "./app.module.css";

import Button from "./components/button";
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

  console.log(form);

  return (
    <div className={css.app}>
      <header className={css.header}>
        <h1>Decision Tree Webapp</h1>
      </header>
      {form && (
        <div>
          <h2>{form.title}</h2>
          <p>{form.question}</p>
          {form.choices.map(({ id, text, next_node_id }) => {
            return (
              <Button
                key={id}
                text={text}
                onClick={() => setId(next_node_id)}
              />
            );
          })}
        </div>
      )}
    </div>
  );
}

export default App;
