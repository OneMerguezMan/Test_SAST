const axios = require('axios');

// SSRF: user controls the entire URL
const targetUrl = process.argv[2];

if (!targetUrl) {
  console.log('Usage: node ssrf.js <url>');
  process.exit(0);
}

axios.get(targetUrl)
  .then((res) => console.log(res.data))
  .catch((e) => console.error('Request failed'));


