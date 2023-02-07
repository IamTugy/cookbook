import React from 'react';
import styled from "styled-components";
import {ColContainer, RowContainer} from "~/common/components/commonStyle";
import {Button, Step, StepContent, StepLabel, Stepper} from "@mui/material";
import {SimpleStep, TimeStep} from "~/store/cookbookApi";
import {deviceType, useDeviceType} from "~/hooks/deviceType";


const StepImage = styled.img`
  height: 10rem;
  margin-right: 1.5rem;
`

const Header = styled.div`
  font-size: 24px;
  font-weight: 600;
  color: #545454;
`


const Instructions = ({steps}: { steps: (SimpleStep | TimeStep)[] }) => {
    const [activeStep, setActiveStep] = React.useState(0);

    const currentDeviceType = useDeviceType()
    const isMobile = currentDeviceType === deviceType.mobile

    const handleNext = () => {
        setActiveStep((prevActiveStep) => prevActiveStep + 1);
    };

    const handleBack = () => {
        setActiveStep((prevActiveStep) => prevActiveStep - 1);
    };

    const handleReset = () => {
        setActiveStep(0);
    };

    return (
        <>
            <Header>Instructions</Header>
            <Stepper activeStep={activeStep} orientation="vertical">
                {steps.map((step, index) => (
                    <Step key={`step-${index}`}>
                        <StepLabel>{step.title}</StepLabel>
                        <StepContent>
                            {isMobile ? <ColContainer>
                                <StepImage alt={step.title} src={step.pictures_url?.[0]}/>
                                {step.description}
                            </ColContainer> : <RowContainer>
                                <StepImage alt={step.title} src={step.pictures_url?.[0]}/>
                                {step.description}
                            </RowContainer>}

                            <Button
                                variant="contained"
                                onClick={handleNext}
                                sx={{mt: 1, mr: 1}}
                            >
                                {index === steps.length - 1 ? 'Finish' : 'Continue'}
                            </Button>
                            <Button
                                disabled={index === 0}
                                onClick={handleBack}
                                sx={{mt: 1, mr: 1}}
                            >
                                Back
                            </Button>
                        </StepContent>
                    </Step>
                ))}
            </Stepper>
        </>
    )
}


export default Instructions
