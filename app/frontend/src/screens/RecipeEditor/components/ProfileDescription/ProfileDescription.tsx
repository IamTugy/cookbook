import React, {useState} from 'react';
import styled from "styled-components";
import {Avatar, Card, CardContent, Link} from "@mui/material";
import {ColContainer, RowContainer} from "~/common/components/commonStyle";
import {Owner} from "~/store/cookbookApi";



const Wrapper = styled(Card)`
  background-color: white;
  color: gray;
  overflow: unset;
`


const ProfileAvatar = styled(Avatar)`
  margin: 0 0.5rem 0.5rem 0;
  height: 5rem;
  width: 5rem;
`

const TopSideWrapper = styled(RowContainer)`
  align-items: center;
  font-size: 16px;
`


interface ReadMoreInterface {
    children: string
}

const TextWrapper = styled.p`
  display: inline;
`;

const ReadMoreWrapper = styled(ColContainer)`
  width: 100%;
  font-size: 13px;
`

const ReadOrHideWrapper = styled.span`
  color: ${props => props.theme.palette.primary.main};
  cursor: pointer;
`;

const ReadMore = ({children}: ReadMoreInterface) => {
    const text = children;
    const maxTextSize = 200;
    const [isReadMore, setIsReadMore] = useState(true);
    const toggleReadMore = () => setIsReadMore(!isReadMore)

    return (
        <ReadMoreWrapper>
            <TextWrapper>
                {isReadMore ? `${text.slice(0, maxTextSize)}...` : text}
            </TextWrapper>
            <ReadOrHideWrapper onClick={toggleReadMore}>
                {isReadMore ? "read more" : "show less"}
            </ReadOrHideWrapper>
        </ReadMoreWrapper>
    )
};

const ProfileNameLink = styled(Link)`
  text-transform: capitalize;
`

const ProfileDescription = ({owner}: {owner: Owner}) => {
    return (
        <Wrapper>
            <CardContent>
                <TopSideWrapper>
                    <ProfileAvatar src={owner.profile_picture}/>
                    <ColContainer>
                        Chef
                        <ProfileNameLink>{owner.english_name}</ProfileNameLink>
                    </ColContainer>
                </TopSideWrapper>
                <ReadMore>{owner.description}</ReadMore>
            </CardContent>
        </Wrapper>
    )
}

export default ProfileDescription
