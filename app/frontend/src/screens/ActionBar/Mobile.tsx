import React from 'react'
import styled from "styled-components"
import {RowContainer} from "~/common/components/commonStyle";


const Wrapper = styled(RowContainer)`
  background-color: white;
  color: black;
  height: 3rem;
  align-items: center;
  justify-content: center;
`


const ActionBarMobile = () => {
    return (
        <Wrapper>
            Mobile Actions Bar
        </Wrapper>
    )
}

export default ActionBarMobile
