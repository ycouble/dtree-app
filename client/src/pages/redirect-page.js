import React, { useState, useEffect } from "react";
import { Redirect } from "react-router-dom";
import queryString from "query-string";

import { RedirectButton } from "../components";
import css from "./css/no-match-page.module.css";

import { redirect } from "../services/api";

const RedirectPage = ({ ...props }) => {
  const [redirection, setRedirection] = useState();

  useEffect(() => {
    const getData = async () => {
      const body = queryString.parse(props.location.search);
      const results = await redirect(body);

      setRedirection(results);
    };

    getData();
  }, [props.location.search]);

  return (
    <div className={css.page}>
      {redirection &&
        (redirection.authorized ? (
          <Redirect to={{ pathname: "/upload" }} />
        ) : (
          <div>
            <h2>{redirection.error}</h2>
            {redirection.error_description.split("\n").map((i, key) => {
              return <p key={key}>{i}</p>;
            })}
            <RedirectButton text={"Back to login page"} type={"logout"} />
          </div>
        ))}
    </div>
  );
};

export default RedirectPage;
