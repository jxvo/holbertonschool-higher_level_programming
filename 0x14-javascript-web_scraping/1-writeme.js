#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

const path = args[0];
const data = args[1];

fs.writeFile(path, data, 'utf8', (err) => {
  if (err) { console.log(err); }
});
