#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Error:');
  process.exit(1);
}
// makes a request to the choosen url
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  // wright the body response to selected file
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error('Error:', err);
      process.exit(1);
    }
    console.log(`Contents of ${url} saved to ${filePath}`);
  });
});
