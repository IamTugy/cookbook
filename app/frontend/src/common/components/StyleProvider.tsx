import React from 'react'
import {createGlobalStyle, ThemeProvider} from 'styled-components'
import {createTheme, ThemeProvider as MuiThemeProvider} from '@mui/material/styles'
import StyledEngineProvider from '@mui/material/StyledEngineProvider'


export const GlobalProvider = createGlobalStyle`
  html, body, #root {
    height: 100%;
    width: 100%;
    overflow: hidden;
    margin: 0;
    display: flex !important;
    font-family: 'Poppins', sans-serif;
  }
`

const StyleProvider = ({children}: { children: React.ReactElement }) => {
  const theme = createTheme({
    palette: {
      primary: {
        main: '#70A344',
        contrastText: 'white',
      },
      secondary: {
        main: '#43a047',
      },
      error: {
        main: '#bb0000',
      }
    },
  });

  return (
      <StyledEngineProvider injectFirst>
        <MuiThemeProvider theme={theme}>
          <ThemeProvider theme={theme}>
            <GlobalProvider/>
            {children}
          </ThemeProvider>
        </MuiThemeProvider>
      </StyledEngineProvider>
  )
}


export default StyleProvider
