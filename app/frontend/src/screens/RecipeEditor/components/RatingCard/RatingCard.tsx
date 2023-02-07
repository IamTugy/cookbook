import React, {useState} from 'react';
import styled from "styled-components";
import {Card, CardContent} from "@mui/material";
import {RowContainer} from "~/common/components/commonStyle";
import Stack from "@mui/material/Stack";
import Rating from "@mui/material/Rating";
import {RatingProps} from "@mui/material/Rating/Rating";


const Wrapper = styled(Card)`
  background-color: white;
  color: gray;
  overflow: unset;
`

const Headers = styled(RowContainer)`
  font-size: 16px;
  font-weight: 500;
`


const ReviewsStyle = styled.div`
  font-size: 14px;
  margin-left: 1rem;
  color: #505050;
  font-weight: 200;
`

const RatingWrapper = styled(RowContainer)`
  align-items: flex-end;
`


const CounterWrapper = styled(RowContainer)`
  color: ${props => props.theme.palette.primary.main};
  padding-left: 0.3rem;
`

interface defaultValue extends RatingProps {
    defaultValue: number
    readOnly?: boolean
    reviews?: number
}

export const HalfRating = ({defaultValue, reviews, readOnly=false, ...props}: defaultValue) => {
    return (
        <RatingWrapper>
            <Stack spacing={1}>
                <Rating defaultValue={defaultValue} precision={0.5} readOnly={readOnly} {...props}/>
            </Stack>
            {reviews ? <ReviewsStyle>
                {reviews} Reviews
            </ReviewsStyle> : null}
        </RatingWrapper>
    )
}

const RatingCard = () => {
    const chefReviewsDefault = 0;
    const recipeReviewsDefault = 0;
    const [chefReviews, setChefReviews] = useState(chefReviewsDefault)
    const [recipeReviews, setRecipeReviews] = useState(recipeReviewsDefault)
    return (
        <Wrapper>
            <CardContent>
                <Stack spacing={1.5}>
                    <Headers>
                        Rate this chef
                    </Headers>
                    <RowContainer>
                        <HalfRating defaultValue={chefReviewsDefault} onChange={(event, newValue) => setChefReviews(newValue || 0)}/>
                        <CounterWrapper>({chefReviews}/5)</CounterWrapper>
                    </RowContainer>
                    <Headers>
                        Rate this recipe
                    </Headers>
                    <RowContainer>
                        <HalfRating defaultValue={recipeReviewsDefault} onChange={(event, newValue) => setRecipeReviews(newValue || 0)}/>
                        <CounterWrapper>({recipeReviews}/5)</CounterWrapper>
                    </RowContainer>
                </Stack>
            </CardContent>
        </Wrapper>
    )
}

export default RatingCard
