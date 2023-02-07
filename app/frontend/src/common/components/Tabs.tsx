import * as React from 'react';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Box from '@mui/material/Box';


interface BasicTabsInterface {
    onChange: (event: React.SyntheticEvent, value: any) => void
    value: number
    tabs: string[]
}

export default function BasicTabs({tabs, value, onChange}: BasicTabsInterface) {
  return (
    <Box sx={{ width: '100%' }}>
      <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
        <Tabs value={value} onChange={onChange} aria-label="basic tabs example">
          {tabs.map((tab: string) => <Tab label={tab}/>)}
        </Tabs>
      </Box>
    </Box>
  );
}
