import _ from 'lodash';
import React from 'react';
import styled from 'styled-components';
import CardContent from '@mui/material/CardContent';
import {ColContainer, RowContainer} from "~/common/components/commonStyle";
import {Card, Stack} from "@mui/material";
import {NutritionValue, RecipeAdditionalInformation} from "~/store/cookbookApi";


const Wrapper = styled(Card)`
  background-color: ${props => props.theme.palette.primary.main};
  color: ${props => props.theme.palette.primary.contrastText};
  
  font-size: 16px;
  font-weight: 300;
`

const Header = styled.div`
   margin-bottom: 10px;
  font-weight: 500;
`

const SubHeader = styled.div`
   margin-bottom: 20px;
  font-size: 13px;
 `


const Line = styled.hr`
  background: rgba(255,255,255,0.65);
  height: 2px;
  width: 100%;
  border-style: hidden;
  margin-top: 0.1rem;
`


const NutritionValueWrapper = styled.div`
  display: flex;
  flex-direction: column;
  width: 50%;
`


const NutritionColumns = styled(RowContainer)`
    justify-content: space-around;
`

const NutritionValueAndType = styled(RowContainer)`
`


export interface NutritionalInformationInterface {
    nutrition?: NutritionValue[]
}

interface NutritionComponentInterface {
    name: string
    value: number
    type?: string
}

const NutritionComponent = ({name, value, type}: NutritionComponentInterface) => {
    return (
        <NutritionValueWrapper>
            <div>{name}</div>
            <NutritionValueAndType>{`${value} ${type || ''}`}</NutritionValueAndType>
            <Line/>
        </NutritionValueWrapper>
    )
}

const NutritionalInformation = ({nutrition}: NutritionalInformationInterface) => {
    if (!(nutrition?.length))
        return null

    const len = nutrition.length
    const isOdd = len % 2
    const informationHalf = len / 2 + isOdd

    return (
        <Wrapper>
            <CardContent>
                <Header>Nutritional Information</Header>
                <NutritionColumns>
                    <ColContainer>
                        <Stack spacing={1}>
                            {nutrition.slice(0, informationHalf).map((info, index) => <NutritionComponent name={info.name} key={`left-nutrition-${index}`} value={info.value} type={info.scale}/>)}
                        </Stack>
                    </ColContainer>
                    <ColContainer>
                        <Stack spacing={1}>
                            {nutrition.slice(informationHalf).map((info, index) => <NutritionComponent name={info.name} key={`right-nutrition-${index}`} value={info.value} type={info.scale}/>)}
                        </Stack>
                    </ColContainer>
                </NutritionColumns>
            </CardContent>
        </Wrapper>
    )
}

export default NutritionalInformation
