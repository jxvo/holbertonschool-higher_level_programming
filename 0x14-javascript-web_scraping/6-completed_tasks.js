#!/usr/bin/node
// compute number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

const arr = [];
const dict = {};

request.get(url, (err, resp, body) => {
  if (err) throw err;
  for (const item of JSON.parse(body)) {
    if (item.completed === true) {
      arr.push(item.userId);
    }
  }
  const set = new Set(arr);
  set.forEach((value) => {
    dict[value] = 0;
  });
  for (const item of JSON.parse(body)) {
    if (item.completed === true) {
      dict[item.userId]++;
      // dict[item.userId].push(item.completed);
    }
  }
  console.log(dict);
});
