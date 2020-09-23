#!/usr/bin/node
const request = require('request');
const todoApi = process.argv[2];
const options = {
  url: todoApi,
  headers: {
    'User-Agent': 'Boss'
  }
};
const report = {};
request.get(options, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const todos = JSON.parse(body);
  for (const task of todos) {
    if (task.completed) {
      if (report[task.userId]) {
        report[task.userId]++;
      } else {
        report[task.userId] = 1;
      }
    }
  }
  console.log(report);
});
