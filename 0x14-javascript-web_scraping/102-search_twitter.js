#!/usr/bin/node

const request = require('request');
let options = {
  method: 'POST',
  url: 'https://api.twitter.com/oauth2/token',
  auth: { user: process.argv[2], pass: process.argv[3] },
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
  },
  body: 'grant_type=client_credentials'
};
request(options, function (error, response, body) {
  if (error) { return; }

  const bearer = JSON.parse(body).access_token;
  options = {
    method: 'GET',
    url: 'https://api.twitter.com/1.1/search/tweets.json',
    auth: { bearer: bearer },
    qs: { q: process.argv[4], count: 5 },
    json: true
  };
  request(options, function (error, response, body) {
    if (error) { return; }

    for (const tweet of body.statuses) {
      console.log(`[${tweet.id}] ${tweet.text} by ${tweet.user.name}`);
    }
  });
});
