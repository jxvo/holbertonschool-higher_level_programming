#!/usr/bin/node
// GET website body and store contents in file

const request = require('request');
const fs = require('fs');

const args = process.argv.slice(2);
const url = args[0];
const path = args[1];

request.get(url, (err, resp, body) => {
  if (err) throw err;
  fs.writeFile(path, body, 'utf8', (error) => {
    if (error) throw error;
  });
});
