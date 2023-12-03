#!/usr/local/bin/node
const request = require('request');
const apiUrl = process.argv[2];
if (!apiUrl) {
  console.error('Error', error.message);
  process.exit(1);
}
const characterId = '18';
// makes request to SW API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  // parse the JSON response
  const data = JSON.parse(body);
  // filter movies where Wedge Salad is present
  const moviesWithWedge = data.results.filter(movie =>
    movie.characters.includes(`${characterId}`));
    // print the # of movies w/ Wedge Salad
  console.log(`${moviesWithWedge.length}`);
});
