import React from "react";

import Button from "./button";

import { login, logout, login_url, redirect_url } from "../services/api";

const RedirectButton = ({ text, type }) => {
  const onRedirectClick = async () => {
    const body = {
      redirect_url: type === "login" ? redirect_url : login_url,
    };
    if (type === "login") {
      const results = await login(body);
      if (results?.auth_uri) window.location.href = results.auth_uri;
    } else if (type === "logout") {
      const results = await logout(body);
      if (results?.logout_uri) window.location.href = results.logout_uri;
    }
  };

  return (
    <Button
      text={text}
      onClick={() => {
        onRedirectClick();
      }}
    />
  );
};

export default RedirectButton;
