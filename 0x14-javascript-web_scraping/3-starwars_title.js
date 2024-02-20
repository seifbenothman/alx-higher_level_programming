#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
