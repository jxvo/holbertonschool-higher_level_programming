#!/usr/bin/node
// print all characters of a Star Wars movie

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) { return; }
  const characterList = JSON.parse(body).characters;
  for (let index = 0; index < characterList.length; index++) {
    request(characterList[index], function (error, response, body) {
      if (error) { return; }
      console.log(JSON.parse(body).name);
    });
  }
});
