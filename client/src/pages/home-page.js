import React, { useState, useEffect } from "react";

import { Button, NodeDescription } from "../components";
import css from "./css/home-page.module.css";

import { getNode } from "../services/api";

const HomePage = ({ setAppName }) => {
  const [form, setForm] = useState();
  const [nodeId, setId] = useState();

  useEffect(() => {
    const getData = async () => {
      const body = {
        id: nodeId,
      };
      console.log(body);
      const results = await getNode(body);

      console.log(results);
      setForm(results);
    };

    getData();
  }, [nodeId]);

  useEffect(() => {
    if (form?.type === "APP_NAME") {
      setId(form.children[0].id);
      setAppName(form.title);
    }
  }, [form]);

  return (
    <div className={css.page}>
      {form && (
        <div>
          <h2>{form.title}</h2>
          {form.description ? (
            <div>
              <NodeDescription text={form.description} />
              {form.children.length != 0 && (
                <Button
                  text={"Suivant"}
                  onClick={() => setId(form.children[0].id)}
                />
              )}
            </div>
          ) : (
            form.children.map(({ id, title, children_id }) => {
              return (
                <Button
                  key={id}
                  text={title}
                  onClick={() => setId(children_id[0])}
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
