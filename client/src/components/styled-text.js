import React from "react";

import css from "./css/styled-text.module.css";

import { reformatStyle } from "../services/string-functions";

const changeStyle = (obj) => {
  if (!obj) return obj;
  for (var key in obj) {
    const newKey = reformatStyle(key);
    if (newKey === key) continue;
    obj[newKey] = obj[key];
    delete obj[key];
  }
  return obj;
};

const StyledText = ({ styledText }) => {
  const offset = styledText.findIndex(({ list }) => {
    return list === "ordered";
  });

  return (
    <div className={css.section}>
      {styledText.map(({ spans, list }, key) => {
        return (
          <div key={key} className={css.line}>
            {list === "bullet" && <div className={css.bullet} />}
            {list === "ordered" && (
              <div className={css.ordered}>{key + offset + 1}.</div>
            )}
            {spans.map(({ style, text }, index) => {
              const string = changeStyle(style?.properties);
              return (
                <span style={string} key={index}>
                  {text}
                </span>
              );
            })}
          </div>
        );
      })}
    </div>
  );
};

export default StyledText;
