import React from 'react'
import styled from "styled-components"
import {RowContainer} from "~/common/components/commonStyle";
import Avatar from "~/screens/TopBar/components/Avatar";
import {deviceType, useDeviceType} from "~/hooks/deviceType";


const TopBarWrapper = styled.div`
  display: flex;
  flex-direction: row;
  background-color: ${props => props.theme.palette.primary.main};
  color: ${props => props.theme.palette.primary.contrastText};
  height: 2rem;
  padding: 1rem;
  align-items: center;
`


const LogoReplacement = styled(RowContainer)`
  font-size: 24px;
  justify-content: center;
  padding-bottom: 0.3rem;
  color: white;
`


const TopBar = () => {
    const currentDeviceType = useDeviceType()
    const isMobile = currentDeviceType === deviceType.mobile

    return (
        <TopBarWrapper>
            <RowContainer stretched>
                <LogoReplacement>Cookbook {isMobile ? 'Mobile' : 'Desktop'}</LogoReplacement>
            </RowContainer>
            <RowContainer>
                <Avatar/>
            </RowContainer>
        </TopBarWrapper>
    )
}

export default TopBar
