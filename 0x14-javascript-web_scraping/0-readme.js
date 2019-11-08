#!/usr/bin/node

const fs = require('fs');
const source = process.argv[2];

fs.readFile(source, 'utf8', (err, source) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(source);
});
