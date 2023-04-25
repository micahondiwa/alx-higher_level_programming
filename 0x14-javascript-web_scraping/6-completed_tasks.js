#!/usr/bin/node
const request = require('request');

request('https://jsonplaceholder.typicode.com/todos', function (err, response, body) {
  if (err == null) {
    const resp = {};
    const json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      if (json[i].completed === true) {
        if (resp[json[i].userId] === undefined) {
          resp[json[i].userId] = 0;
        }
        resp[json[i].userId]++;
      }
    }
    console.log(resp);
  }
