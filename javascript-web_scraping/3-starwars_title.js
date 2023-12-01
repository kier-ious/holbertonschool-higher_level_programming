#!/usr/bin/node
const request = require('request');
const moveId = process.argv[2];
if (!moveId) {
  console.error('Error');
  process.exit(1);
}
const apiUrl = `https://swapi-api.hbtn.io/api/films/${moveId}`;
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
  } else {
    try {
      const movieData = JSON.parse(body);
      console.log(`${movieData.title}`);
    } catch (parseError) {
      console.error('Error:', parseError.message);
    }
  }
});
