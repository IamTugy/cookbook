import React, {useState} from 'react';
import styled from "styled-components";
import {Checkbox, Divider, FormControlLabel} from "@mui/material";
import CheckBoxOutlineBlankIcon from '@mui/icons-material/CheckBoxOutlineBlank';
import CheckIcon from '@mui/icons-material/Check';
import Pluralize from 'pluralize';

import {ColContainer, RowContainer} from "~/common/components/commonStyle";
import {Ingredient} from "~/store/cookbookApi";

const Wrapper = styled(ColContainer)`
`


const Header = styled.div`
  font-size: 24px;
  font-weight: 600;
  color: #545454;
`

const IngredientContainer = styled(RowContainer)`
  font-weight: 200;
  font-size: 15px;
  align-items: center;
  padding: 1rem 0;
`

const StyledCheckboxBlank = styled.div`
  border-style: solid;
  border-radius: 25% 25% 25% 0;
  color: gray;
  height: 20px;
  width: 20px;
`

const StyledCheckboxFilled = styled(CheckIcon)`
  border-radius: 25% 25% 25% 0;
  background-color: ${props => props.theme.palette.primary.main};
  color: ${props => props.theme.palette.primary.contrastText};
  font-size: 26px;
`


interface IngredientItem {
    checked: boolean
    setChecked: (value: boolean) => void
    content: string
}

const IngredientItem = ({checked, setChecked, content}: IngredientItem) => {
    return (
        <ColContainer>
            <IngredientContainer>
                <Checkbox
                    checked={checked}
                    onChange={(event) => setChecked(event.target.checked)}
                    icon={<StyledCheckboxBlank/>}
                    checkedIcon={<StyledCheckboxFilled/>}
                />
                {content}
            </IngredientContainer>
            <Divider/>
        </ColContainer>
    )
}

const Ingredients = ({ingredients}: {ingredients: Ingredient[]}) => {

    const [checked, setChecked] = useState(ingredients.map(() => false))

    const getItemContent = (item: Ingredient) => {
        let content = ''
        if (item.value)
            content = content.concat(`${item.value} `)

        if (item.scale)
            content = content.concat(`${(item.value || 0) > 1 ? Pluralize(item.scale) : item.scale} `)

        if (content && item.scale)
            content = content.concat('of ')

        content = content.concat(item.name)

        return content
    }

    return (
        <Wrapper>
            <Header>Ingredients</Header>
            {ingredients.map((item, index) => <IngredientItem
                checked={checked[index]}
                setChecked={(value) => {
                    const newList = checked.slice()
                    newList[index] = value
                    setChecked(newList)
                }}
                content={getItemContent(item)}
                key={`ingredient-${index}`}
            />)}
        </Wrapper>
    )
}

export default Ingredients
