import {useState, useEffect} from 'react';
import {useMediaQuery, useTheme} from "@mui/material";

export enum deviceType {
    desktop,
    mobile,
    tablet
}

export const useDeviceType = () => {
    const theme = useTheme()
    const [currentDeviceType, setCurrentDeviceType] = useState<number>();
    const isMobile = useMediaQuery(theme.breakpoints.down('md'))

    useEffect(() => {
      if (isMobile)
        setCurrentDeviceType(deviceType.mobile)
      else
        setCurrentDeviceType(deviceType.desktop)
    }, [isMobile]);

    return currentDeviceType;
}
