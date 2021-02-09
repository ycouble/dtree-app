import React, { useState, useEffect } from "react";
import { Route, Redirect } from "react-router-dom";

import { connected } from "./api";

const PrivateRoute = ({ component: Component, ...rest }) => {
  const [isConnected, setIsConnected] = useState();

  useEffect(() => {
    const getData = async () => {
      const results = await connected({});

      setIsConnected(results?.connected);
    };

    getData();
  }, [setIsConnected]);

  return (
    <div>
      {isConnected !== undefined && (
        <Route
          {...rest}
          render={() =>
            isConnected === true ? (
              <Component />
            ) : (
              <Redirect to={{ pathname: "/login" }} />
            )
          }
        />
      )}
    </div>
  );
};

export default PrivateRoute;
