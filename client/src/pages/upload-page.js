import React from "react";

import { RedirectButton } from "../components";
import css from "./css/no-match-page.module.css";

const UploadPage = () => {
  return (
    <div className={css.page}>
      <RedirectButton text={"Logout"} type={"logout"} />
    </div>
  );
};

export default UploadPage;
