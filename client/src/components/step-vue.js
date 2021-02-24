import React from "react";

import NextButton from "./next-button";
import css from "./css/step-vue.module.css";

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

const StepVue = ({ description, attachements, children }) => {
  return (
    <div>
      <div className={css.paragraphe}>
        {description.map(({ spans }, key) => {
          return (
            <div key={key} className={css.line}>
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
      <div>
        {attachements?.map(({ id, title, href }) => {
          return <div key={id}>{title + " -> " + href}</div>;
        })}
        {children.length !== 0 && (
          <NextButton to={`/dtree/${children[0].id}`} />
        )}
      </div>
    </div>
  );
};

export default StepVue;
