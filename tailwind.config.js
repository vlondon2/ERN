module.exports = {
  mode: "jit",
  content: [
    "./src/**/**/*.{js,ts,jsx,tsx,html,mdx}",
    "./src/**/*.{js,ts,jsx,tsx,html,mdx}",
  ],
  darkMode: "class",
  theme: {
    screens: { md: { max: "1050px" }, sm: { max: "550px" } },
    extend: {
      colors: {
        bluegray_900: "#22194d",
        gray_700: "#556561",
        red_700: "#d92525",
        black_900: "#000000",
        gray_800: "#4e4e4e",
        teal_900: "#044040",
        red_700_99: "#d9252599",
        red_700_cc: "#d92525cc",
        white_A700: "#ffffff",
        gray_100: "#f2f2f2",
      },
      fontFamily: { manrope: "Manrope" },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
