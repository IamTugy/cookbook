import React from 'react';
import styled from 'styled-components';

import NutritionalInformation, {NutritionalInformationInterface} from './Nutrition';
import {ComponentMeta} from "@storybook/react";

export default {
  title: 'Components/RecipeEditor/NutritionalInformation',
  component: NutritionalInformation,
  argTypes: {
    recipeId: { control: 'number' },
  },
  args: {
    recipeId: 1,
  },
} as ComponentMeta<typeof NutritionalInformation>;

const Wrapper = styled.div`
  height: auto;
  width: 300px;
`;

const Template = (args: NutritionalInformationInterface) => (<Wrapper><NutritionalInformation {...args} /></Wrapper>);

export const Base = Template.bind({});
