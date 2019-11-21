const url =
  'https://drive.google.com/file/d/1PDuXSWsJ6ZIPM-EXSiOSVcJczA5dVpN7/view?usp=drivesdk'
var res = url.split('https://drive.google.com/file/d/')
res = res[1]
res = res.split('/view?usp=drivesdk')

console.log("https://drive.google.com/uc?id=" + res[0])
console.log("https://drive.google.com/uc?id=" + res[0])
