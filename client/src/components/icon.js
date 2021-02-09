import React from "react";

import css from "./css/icon.module.css";

const Icon = ({ path }) => {
  return <img className={css.icon} src={path} alt="" />;
};

export default Icon;
