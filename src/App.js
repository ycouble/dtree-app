import React from "react";
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

function App() {
  return (
    <div className={css.app}>
      <header className={css.header}>
        <h1>Decision Tree Webapp</h1>
      </header>
      <Switch>
        <Route exact path={"/"} component={() => <HomePage />} />
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
