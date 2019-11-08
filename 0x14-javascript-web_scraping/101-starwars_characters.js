#!/usr/bin/node
// return list of names of characters from movie in order (sync)

const request = require('request');
const id = process.argv[2];

const url = 'http://swapi.co/api/films/' + id;
const charDict = {};

request.get(url, (err, response, body) => {
  if (err) { return; }
  const charList = JSON.parse(body).characters;
  let count = 0;
  for (let i = 0; i < charList.length; i++) {
    request.get(charList[i], (err, response, body) => {
      if (err) { return; }
      const person = JSON.parse(body);
      charDict[person.url] = person.name;
      count++;
      if (count === charList.length) {
        for (const charURL of charList) {
          console.log(charDict[charURL]);
        }
      }
    });
  }
});
