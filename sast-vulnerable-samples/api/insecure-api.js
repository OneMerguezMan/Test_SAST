const https = require('https');

// Hardcoded API token and disabled TLS verification
const API_TOKEN = 'Bearer hardcoded-insecure-token';
process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';

// User-provided path appended directly to base URL
const base = 'https://public-api.example.com';
const path = process.argv[2] || '/v1/search?q=foo';

const options = {
  method: 'GET',
  headers: { 'Authorization': API_TOKEN }
};

https.get(base + path, options, res => {
  res.on('data', d => process.stdout.write(d));
}).on('error', () => {
  console.error('request failed');
});


