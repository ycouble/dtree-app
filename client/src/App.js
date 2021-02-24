import React, { useState, useEffect } from "react";
import { Switch, Route, Redirect } from "react-router-dom";

import {
  DtreePage,
  LoginPage,
  NoMatchPage,
  RedirectPage,
  UploadPage,
} from "./pages/index";
import { getNode, getCurrentID } from "./services/api";
import { getRootNode } from "./services/dtree";
import PrivateRoute from "./services/private-route";
import css from "./app.module.css";

// TODO: Change update on header name
const App = () => {
  const [dtree, setDTree] = useState(
    JSON.parse(localStorage.getItem("dtree")) || undefined
  );
  const [appName, setAppName] = useState("Decision Tree Webapp");

  const fetchDTree = async () => {
    const results = await getNode({});
    setDTree(results);
    localStorage.setItem("dtree", JSON.stringify(results));
  };

  useEffect(() => {
    const getID = async (id) => {
      const currentID = await getCurrentID();
      if (currentID !== id) fetchDTree();
    };

    const dtreeID = dtree?.id;
    if (dtreeID) getID(dtreeID);
    else fetchDTree();

    if (dtree) setAppName(getRootNode(dtree).title);
  }, [dtree]);

  return (
    <div className={css.app}>
      <header className={css.header}>
        <h1>{appName}</h1>
      </header>
      <Switch>
        <Route exact path="/">
          <Redirect to={`/dtree`} />
        </Route>
        <Route
          path={"/dtree"}
          component={() => (dtree ? <DtreePage dtree={dtree} /> : <div />)}
        />
        <Route exact path={"/login"} component={() => <LoginPage />} />
        <Route
          exact
          path={"/redirect"}
          component={(props) => <RedirectPage {...props} />}
        />
        <PrivateRoute exact path={"/upload"} component={() => <UploadPage />} />
        <Route component={NoMatchPage} />
      </Switch>
    </div>
  );
};

export default App;
