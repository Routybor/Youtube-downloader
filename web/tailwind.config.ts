import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  daisyui: {
    themes: [
      {
        mytheme: {
          primary: '#0031ff',
          secondary: '#3e5eff',
          accent: '#cc0000',
          neutral: '#1b0f00',
          'base-100': '#fffef8',
          info: '#008b9d',
          success: '#008a2e',
          warning: '#ff9900',
          error: '#db002b',
        },
      },
    ],
  },
  plugins: [require('daisyui')],
}
export default config
