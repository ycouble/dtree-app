import React, { useState, useEffect } from "react";
import { Redirect } from "react-router-dom";
import queryString from "query-string";

import css from "./css/no-match-page.module.css";

import { redirect } from "../services/api";

const RedirectPage = ({ ...props }) => {
  const [redirection, setRedirection] = useState();

  useEffect(() => {
    const getData = async () => {
      const body = queryString.parse(props.location.search);
      const results = await redirect(body);

      setRedirection(results?.authorized);
    };

    getData();
  }, [props.location.search]);

  return (
    <div className={css.page}>
      {redirection && <Redirect to={{ pathname: "/upload" }} />}
    </div>
  );
};

export default RedirectPage;
