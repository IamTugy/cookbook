import {Auth0Provider} from '@auth0/auth0-react';
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {Provider} from "react-redux";
import {store} from "~/store";
import Auth0ProviderWithHistory from "~/Auth0ProviderWithHistory";
import {BrowserRouter} from "react-router-dom";

const root = ReactDOM.createRoot(
    document.getElementById('root') as HTMLElement
);


root.render(
    <React.StrictMode>
        <Provider store={store}>
            <BrowserRouter>
                <Auth0ProviderWithHistory>
                    {/*<Auth0Provider*/}
                    {/*    domain="dev-8vhgxnbl80hnu7hv.us.auth0.com"*/}
                    {/*    clientId="T3TO1oDPJUYLUM0Z5gSasxDFCk8sfFUB"*/}
                    {/*    authorizationParams={{*/}
                    {/*        redirect_uri: window.location.origin,*/}
                    {/*        scope: "openid profile email phone"*/}
                    {/*    }}*/}
                    {/*>*/}
                        <App/>
                    {/*</Auth0Provider>*/}
                </Auth0ProviderWithHistory>
            </BrowserRouter>
        </Provider>
    </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
