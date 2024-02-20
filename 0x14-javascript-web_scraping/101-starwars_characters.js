#!/usr/bin/node

const req = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

req.get(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    const chars = data.characters;
    let i = 0;

    const printChar = () => {
      if (i < chars.length) {
        const charUrl = chars[i];
        req.get(charUrl, (err, resp, body) => {
          if (err) {
            console.error(err);
          } else {
            const charData = JSON.parse(body);
            console.log(charData.name);
            i++;
            printChar();
          }
        });
      }
    };

    printChar();
  }
});
