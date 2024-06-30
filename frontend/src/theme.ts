import { createTheme, MantineColorsTuple } from '@mantine/core';

const customColors: MantineColorsTuple = [
  '#fceeff',
  '#efdbf6',
  '#dab5e6',
  '#c58ed6',
  '#b26cc9',
  '#a756c1',
  '#a14abe',
  '#8d3ca8',
  '#7f3496',
  '#6e2a85',
];

const theme = createTheme({
  primaryColor: 'violet',
  colors: {
    violet: customColors,
  },
});

export default theme;
