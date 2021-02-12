import React, { useState, useEffect } from "react";

import { Button, NodeDescription } from "../components";
import css from "./css/home-page.module.css";

import { getNode } from "../services/api";

const HomePage = () => {
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

  const length = form?.choices.length;

  return (
    <div className={css.page}>
      {form && (
        <div>
          <h2>{form.title}</h2>
          <p>{form.question}</p>
          {length === 1 ? (
            <div>
              <NodeDescription text={form.choices[0].text} />
              <div className={css.buttonSet}>
                <Button text={"Télécharger le document"} />
                <Button
                  text={"Suivant"}
                  onClick={() => setId(form.choices[0].next_node_id)}
                />
              </div>
            </div>
          ) : (
            form.choices.map(({ id, text, next_node_id }) => {
              return (
                <Button
                  key={id}
                  text={text}
                  onClick={() => setId(next_node_id)}
                />
              );
            })
          )}
        </div>
      )}
    </div>
  );
};

export default HomePage;
