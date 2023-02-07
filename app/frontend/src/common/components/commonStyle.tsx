import {animated} from 'react-spring'
import styled, {css} from 'styled-components'


const commonStyle = css<{ stretched?: boolean, scrollable?: boolean }>`
  display: flex;
  position: relative;
  flex: ${({stretched}) => stretched ? 1 : undefined};
  overflow: ${({scrollable}) => scrollable ? 'auto' : undefined};
  min-height: 0;
  min-width: 0;
  flex-shrink: 0;
`

export const RowContainer = styled.div`
  ${commonStyle}
`

export const AnimatedRowContainer = styled(animated.div)`
  ${commonStyle}
`

export const ColContainer = styled(RowContainer)`
  flex-direction: column;
`
