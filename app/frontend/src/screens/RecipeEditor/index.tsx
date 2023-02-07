import React, {useState} from 'react';
import styled from "styled-components";
import PrintOutlined from '@mui/icons-material/PrintOutlined';
import ShareOutlined from '@mui/icons-material/ShareOutlined';
import EditOutlined from '@mui/icons-material/EditOutlined';
import CloseOutlined from '@mui/icons-material/CloseOutlined';
import BackspaceOutlined from '@mui/icons-material/BackspaceOutlined';
import {ColContainer, RowContainer} from "~/common/components/commonStyle";
import NutritionalInformation from "~/screens/RecipeEditor/components/Nutrition/Nutrition";
import {Button, Chip, Divider, TextField} from "@mui/material";
import Stack from '@mui/material/Stack';
import ImageGallery from "~/screens/RecipeEditor/components/ImageGallery/ImageGallery";
import ProfileDescription from "~/screens/RecipeEditor/components/ProfileDescription/ProfileDescription";
import RatingCard, {HalfRating} from "~/screens/RecipeEditor/components/RatingCard/RatingCard";
import {deviceType, useDeviceType} from "~/hooks/deviceType";
import Ingredients from "~/screens/RecipeEditor/components/Ingredients/Ingredients";
import {Recipe, RecipeAdditionalInformation, useGetRecipesByIdRecipesRecipeIdGetQuery} from "~/store/cookbookApi";
import {useAuth0, withAuthenticationRequired} from "@auth0/auth0-react";
import Instructions from "~/screens/RecipeEditor/components/Instructions/Innstructions";



const RecipeChip = styled(Chip)`
  background-color: ${props => props.theme.palette.primary.main};
  color: ${props => props.theme.palette.primary.contrastText};
  border-radius: 0;
  min-width: 6rem;
  margin: 0.8rem 0.2rem;
  font-weight: bold;
`


const RecipeTags = ({tags}: { tags: string[] }) => {
    return (
        <RowContainer>
            {tags.map((tag, index) => <RecipeChip key={`tag-${index}`} label={tag}/>)}
        </RowContainer>
    )
}

const RecipeEditorWrapper = styled(ColContainer)<{ isMobile: boolean }>`
  background: #F5F5F5;
  padding: ${props => props.isMobile ? "0.5rem" : "2rem"};
`

const Title = styled.div`
  display: flex;
  flex: 1;
  font-size: 26px;
  color: #505050;
  margin-bottom: 0.5rem;
`

const SubTitle = styled.div`
  font-size: 20px;
  color: #505050;
  margin-bottom: 0.5rem;
`


const MainSectionWrapper = styled(ColContainer)`
  margin-right: 1.4rem;
  flex: 8
`


const RightSectionWrapper = styled(ColContainer)`
  flex: 3;
  min-width: 15rem;
`


const ShareButton = styled(Button)`
  background: white;
  border-color: #00000010;
  color: #797979;
  text-transform: capitalize;
  min-width: 5rem;

  & .MuiButton-endIcon svg {
    color: ${props => props.theme.palette.primary.main};
  }
`

const PrintButton = styled(ShareButton)`
`

const EditButton = styled(ShareButton)`
`

const CancelEditButton = styled(ShareButton)`
  & .MuiButton-endIcon svg {
    color: ${props => props.theme.palette.error.main};
  }
`

const ResetEditButton = styled(CancelEditButton)`
`

const AdditionalInfoWrapper = styled(Stack)`
  background-color: white;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  font-size: 14px;
`

const InfoItemStyle = styled(Stack)`
  height: 2rem;
  align-items: center;
`

const InfoKeyStyle = styled.div`
  color: ${props => props.theme.palette.primary.main};
`

const AdditionalInfo = ({additionalInfo}: {additionalInfo: RecipeAdditionalInformation}) => {
    return (
        <AdditionalInfoWrapper spacing={1} direction="row">
                <InfoItemStyle direction="row" spacing={1}>
                    <InfoKeyStyle>Servings:</InfoKeyStyle>
                    <div>{additionalInfo.servings}</div>
                    <Divider orientation="vertical" variant="middle" flexItem/>
                    <InfoKeyStyle>Prep Time:</InfoKeyStyle>
                    <div>{additionalInfo.prep_time} min</div>
                    <Divider orientation="vertical" variant="middle" flexItem/>
                    <InfoKeyStyle>Work Time:</InfoKeyStyle>
                    <div>{additionalInfo.work_time} min</div>
                </InfoItemStyle>
        </AdditionalInfoWrapper>
    )
}

const LayoutByDevice = ({data}: {data: Recipe}) => {
    const currentDeviceType = useDeviceType()
    const isMobile = currentDeviceType === deviceType.mobile

    return isMobile ? (
        <ColContainer>
            <Stack spacing={2}>
                <ImageGallery pictureUrls={data.pictures_url}/>
                <ProfileDescription owner={data.owner}/>
                <RatingCard/>
                <NutritionalInformation nutrition={data.nutrition}/>
                <AdditionalInfo additionalInfo={data.additional_info}/>
                <Ingredients ingredients={data.ingredients}/>
            </Stack>
        </ColContainer>
    ) : (
        <RowContainer>
            <MainSectionWrapper>
                <Stack spacing={3}>
                    <ImageGallery pictureUrls={data.pictures_url}/>
                    <AdditionalInfo additionalInfo={data.additional_info}/>
                    <Ingredients ingredients={data.ingredients}/>
                </Stack>
            </MainSectionWrapper>
            <RightSectionWrapper>
                <Stack spacing={2}>
                    <ProfileDescription owner={data.owner}/>
                    <RatingCard/>
                    <NutritionalInformation nutrition={data.nutrition}/>
                </Stack>
            </RightSectionWrapper>
        </RowContainer>
    )
}


const TopActionsContainer = styled(RowContainer)<{ isMobile: boolean }>`
  align-items: ${props => props.isMobile ? "flex-end" : "flex-start"};
  justify-content: ${props => props.isMobile ? "flex-start" : "flex-end"};
  flex-direction: ${props => props.isMobile ? "column" : "row"};
`


const RecipeEditor = () => {
    const [editMode, setEditMode] = useState(false)

    const currentDeviceType = useDeviceType()
    const isMobile = currentDeviceType === deviceType.mobile
    const {data, isLoading, isFetching, isError} = useGetRecipesByIdRecipesRecipeIdGetQuery({recipeId: 1}, {
        pollingInterval: 10000,
        refetchOnMountOrArgChange: true,
        skip: false,
    })

    if (!data) {
        return <>No Data</>
    }

    const flipEditMode = () => setEditMode(!editMode)

    return (
        <RecipeEditorWrapper stretched scrollable isMobile={isMobile}>
            <RowContainer>
                <Title>{editMode ? <TextField variant="standard" label="Title" defaultValue={data.title} /> : data.title}</Title>
                <TopActionsContainer isMobile={isMobile}>
                    {editMode ? (
                        <>
                            <ResetEditButton
                                variant="outlined"
                                endIcon={<BackspaceOutlined/>}
                            >
                                Reset
                            </ResetEditButton>
                            <CancelEditButton
                                variant="outlined"
                                endIcon={<CloseOutlined/>}
                                onClick={flipEditMode}
                            >
                                Cancel
                            </CancelEditButton>
                        </>
                    ) : (
                        <>
                            <PrintButton variant="outlined" endIcon={<PrintOutlined/>}>Print</PrintButton>
                            <ShareButton variant="outlined" endIcon={<ShareOutlined/>}>Share</ShareButton>
                            <EditButton variant="outlined" endIcon={<EditOutlined/>}
                                        onClick={flipEditMode}>Edit</EditButton>
                        </>
                    )}

                </TopActionsContainer>
            </RowContainer>
            <SubTitle>{data.description}</SubTitle>
            {!editMode && <HalfRating defaultValue={3.5} reviews={362} readOnly/>}
            {data.tags && <RecipeTags tags={data.tags}/>}
            <Stack spacing={2}>
                <LayoutByDevice data={data}/>
                <Instructions steps={data.sections}/>
            </Stack>
        </RecipeEditorWrapper>
    )
}

export default withAuthenticationRequired(RecipeEditor, {
  onRedirecting: () => <>Not logged in</>})
