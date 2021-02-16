import React, { useState } from "react";
import { Switch, Route } from "react-router-dom";

import {
  HomePage,
  LoginPage,
  NoMatchPage,
  RedirectPage,
  UploadPage,
} from "./pages/index";
import PrivateRoute from "./services/private-route";
import css from "./app.module.css";

// TODO: Change update on header name
function App() {
  const [appName, setAppName] = useState("Decision Tree Webapp");
  return (
    <div className={css.app}>
      <header className={css.header}>
        <h1>{appName}</h1>
      </header>
      <Switch>
        <Route
          exact
          path={"/"}
          component={() => <HomePage setAppName={setAppName} />}
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
}

export default App;
