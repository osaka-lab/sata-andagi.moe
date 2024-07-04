/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        "montserrat": ["Montserrat"]
      },
      colors: {
        ananasGold: {
          DEFAULT: "#ffcb00",
          100: "#ffde00",
          400: "#ffcb00",
          800: "#cca300"
        },
        exeBlack: "#090b11",
        exeGray: "#9ca3af",
        goldyPink: "#fb89ab",
        goldyDarky: {
            DEFAULT: "#0e1114",
            200: "#0e1114",
            300: "#0b0d0f",
            500: "#0a0b0d",
        },
        goldyGreyy: {
            DEFAULT: "#222930",
            100: "#222930",
            300: "#2A2B2C"
        },
        goldyCream: {
            DEFAULT: "#fbc689",
            200: "#fbc689",
            800: "theme(colors.orange.50)"
        },
        goldyWhite: "#f1f1f1",
        goldyOrangy: {
            DEFAULT: "#f5671b",
            100: "#f5671b",
            300: "#f57d3d",
            800: "#f5be3d"
        },
        goldyGreen: "#d0f54c"
      },
      screens: {
        "mobile": {"max": "430px"},
        "tablet": {"max": "850px"},
        "desktop": {"max": "1280px"}
      },
    }
  },
}