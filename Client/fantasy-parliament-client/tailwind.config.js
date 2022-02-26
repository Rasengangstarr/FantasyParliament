module.exports = {
  content: ["./src/**/*.js"],
  theme: {
    colors: {
    'nord-dark-1':'#2E3440',
     'nord-dark-2':'#3B4252',
     'nord-dark-3':'#434C5E',
     'nord-dark-4':'#4C566A',
     'nord-light-1':'#D8DEE9',
     'nord-light-2':'#E5E9F0',
     'nord-light-3':'#ECEFF4',
     'nord-frost-1':'#8FBCBB',
     'nord-frost-2':'#88C0D0',
     'nord-frost-3':'#81A1C1',
     'nord-frost-4':'#5E81AC',
     'nord-red':'#BF616A',
     'nord-orange':'#D08770',
     'nord-yellow':'#EBCB8B',
     'nord-green':'#A3BE8C',
     'nord-purple':'#B48EAD'},
    extend: {},
  },
  plugins: [require('tw-elements/dist/plugin')],
}
