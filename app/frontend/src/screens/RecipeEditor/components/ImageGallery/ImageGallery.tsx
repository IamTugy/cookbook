import React, {useState} from 'react';
import {ColContainer, RowContainer} from "~/common/components/commonStyle";
import styled from "styled-components";

const Wrapper = styled(ColContainer)`
  height: 30rem;
  overflow: hidden;
  background-color: white;
  padding: 0 0.5rem;
`


const BottomScroll = styled(RowContainer)`
  flex: 1;
  overflow-x: scroll;
  margin-top: 0.5rem;

  ::-webkit-scrollbar {
    -webkit-appearance: none;
    height: 0.7rem;
  }
  
  ::-webkit-scrollbar:vertical {
    width: 5px;
  }

  ::-webkit-scrollbar:horizontal {
    width: 5px;
  }

  ::-webkit-scrollbar-thumb {
    border-radius: 8px;
    border: 1px solid white; /* should match background, can't be transparent */
    background-color: rgba(0, 0, 0, .5);
  }
`

const MainImageScroll = styled(RowContainer)`
  flex: 5;
  justify-content: center;
;
`


const SelectableImage = styled.img<{selected: boolean}>`
  cursor: pointer;
  margin-right: 0.4rem;
  border-color: ${props => props.theme.palette.primary.main};
  opacity: ${props => props.selected ? 0.5 : null};
`


const ImageGallery = ({pictureUrls}: {pictureUrls?: string[]}) => {
    if (!pictureUrls)
        return null

    const [index, setIndex] = useState(0)

    const selectedImage = pictureUrls[index]

    return (
        <Wrapper>
            <MainImageScroll>
                <img
                    src={`${selectedImage}?w=161&fit=crop&auto=format`}
                    srcSet={`${selectedImage}?w=161&fit=crop&auto=format&dpr=2 2x`}
                    alt={'none'}
                    loading="lazy"
                />
            </MainImageScroll>
            <BottomScroll>
                {pictureUrls.map((imageUrl, currentIndex) => <SelectableImage
                    src={`${imageUrl}?w=161&fit=crop&auto=format`}
                    srcSet={`${imageUrl}?w=161&fit=crop&auto=format&dpr=2 2x`}
                    alt={'none'}
                    loading="lazy"
                    onClick={() => setIndex(currentIndex)}
                    key={`image-${currentIndex}`}
                    selected={currentIndex === index}
                />)}
            </BottomScroll>
        </Wrapper>
    )
}

export default ImageGallery
