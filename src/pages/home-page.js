import React, { useState, useEffect } from "react";

import { Button } from "../components";
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

  console.log(form);

  return (
    <div className={css.page}>
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
};

export default HomePage;
