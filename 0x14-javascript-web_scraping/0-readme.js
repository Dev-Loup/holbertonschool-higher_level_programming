#!/usr/bin/node
let path = process.argv[2];
var fs = require('fs');

fs.readFile(path, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
