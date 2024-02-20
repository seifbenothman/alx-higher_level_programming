#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    const done = {};

    data.forEach(task => {
      if (task.completed) {
        if (done[task.userId]) {
          done[task.userId]++;
        } else {
          done[task.userId] = 1;
        }
      }
    });

    console.log(done);
  }
});
