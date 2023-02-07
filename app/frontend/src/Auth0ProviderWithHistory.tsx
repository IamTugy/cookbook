import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Auth0Provider } from '@auth0/auth0-react';
import {AppState} from "@auth0/auth0-react/src/auth0-provider";


const Auth0ProviderWithHistory = ({ children }: {children: React.ReactElement}) => {
  const domain = process.env.REACT_APP_AUTH0_DOMAIN;
  const clientId = process.env.REACT_APP_AUTH0_CLIENT_ID;

  const navigate = useNavigate();

  const onRedirectCallback = (appState?: AppState) => {
    navigate(appState?.returnTo || window.location.pathname);
  };

  return (
    <Auth0Provider
      domain={domain || ""}
      clientId={clientId || ""}
      onRedirectCallback={onRedirectCallback}
      authorizationParams={{
          redirect_uri: window.location.origin,
          scope: "openid profile email phone",
      }}
    >
      {children}
    </Auth0Provider>
  );
};

export default Auth0ProviderWithHistory;
