import {addDecorator} from "@storybook/react";
import StyleProvider from "../src/common/components/StyleProvider";

export const parameters = {
  actions: { argTypesRegex: "^on[A-Z].*" },
  controls: {
    matchers: {
      color: /(background|color)$/i,
      date: /Date$/,
    },
  },
}

addDecorator(story => {
  return (
    <StyleProvider>
      {story()}
    </StyleProvider>
  );
});
