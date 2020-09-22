#!/usr/bin/node
let path = process.argv[2];
if (typeof path === 'undefined') {
  path = '';
}
var fs = require('fs');
fs.readFile(path, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
