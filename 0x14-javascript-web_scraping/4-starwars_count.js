#!/usr/bin/node
// Return number of movies that Antellis was in

const request = require('request');
const url = process.argv[2];

let count = 0;
request.get(url, (error, resp, body) => {
  if (error) throw error;
  for (const film of JSON.parse(body).results) {
    for (const line of film.characters) {
      if (line.endsWith('18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
