import React, {useEffect} from "react"
import styled from "styled-components"
import {useAuth0} from "@auth0/auth0-react"

import {ColContainer, RowContainer} from "~/common/components/commonStyle"
import StyleProvider from "~/common/components/StyleProvider"
import {useDispatch} from "react-redux";
import {setToken} from "~/store/slices/userInfoSlice";
import ActionBarDesktop from "~/screens/ActionBar/Desktop";
import RecipeEditor from "~/screens/RecipeEditor";
import TopBar from "~/screens/TopBar";
import ActionBarMobile from "~/screens/ActionBar/Mobile";
import {deviceType, useDeviceType} from "~/hooks/deviceType";
import {createBrowserRouter, RouterProvider} from "react-router-dom";

const AppWrapper = styled(ColContainer)`
    width: 100%;
    padding: 0;
`


const router = createBrowserRouter([
    {
        path: '/',
        element: <RecipeEditor/>
    }
])

export const App = () => {
    const {getAccessTokenSilently, getAccessTokenWithPopup, user} = useAuth0()
    const currentDeviceType = useDeviceType()

    const dispatch = useDispatch()

    console.log({user})

    useEffect(() => {
        (async () => {
            try {
                const token = await getAccessTokenSilently({
                    authorizationParams: {
                        audience: 'cookbook-backend',
                    }
                })
                if (!token)
                    return
                dispatch(setToken(token))
            } catch (e) {
                // Handle errors such as `login_required` and `consent_required` by re-prompting for a login
                console.error(e);
            }
        })()
    }, [getAccessTokenSilently])

    return (
        <StyleProvider>
            <AppWrapper>
                <TopBar/>
                    {currentDeviceType === deviceType.desktop ? (
                        <RowContainer stretched>
                            <ActionBarDesktop/>
                            <RecipeEditor/>
                        </RowContainer>
                    ) : (  // mobile
                        <>
                            <RecipeEditor/>
                            <ActionBarMobile/>
                        </>
                    )}
            </AppWrapper>
        </StyleProvider>
    )
}

export default App
