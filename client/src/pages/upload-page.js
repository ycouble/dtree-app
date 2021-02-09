import React, { useState, useEffect } from "react";

import { Button } from "../components";
import css from "./css/no-match-page.module.css";

import { logout } from "../services/api";

const redirect_url = "http://localhost:3000/login";

const UploadPage = ({}) => {
  const onLogout = async () => {
    const body = {
      redirect_url,
    };
    const results = await logout(body);

    if (results?.logout_uri) window.location.href = results.logout_uri;
  };

  return (
    <div className={css.page}>
      <Button
        text={"Logout"}
        onClick={() => {
          onLogout();
        }}
      />
    </div>
  );
};

export default UploadPage;
