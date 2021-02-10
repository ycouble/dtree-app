import React from "react";

import { RedirectButton } from "../components";
import css from "./css/no-match-page.module.css";

const LoginPage = () => {
  return (
    <div className={css.page}>
      <RedirectButton text={"Login with Microsoft"} type={"login"} />
    </div>
  );
};

export default LoginPage;
