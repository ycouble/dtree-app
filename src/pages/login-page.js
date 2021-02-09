import React from "react";

import { Button } from "../components";
import css from "./css/no-match-page.module.css";

import { login } from "../services/api";

const redirect_url = "http://localhost:3000/redirect";

const LoginPage = ({ setAuth }) => {
  const onLogin = async () => {
    const body = {
      redirect_url,
    };
    const results = await login(body);

    if (results?.auth_uri) window.location.href = results.auth_uri;
  };

  return (
    <div className={css.page}>
      <Button
        text={"Login with Microsoft"}
        onClick={() => {
          onLogin();
        }}
      />
    </div>
  );
};

export default LoginPage;
