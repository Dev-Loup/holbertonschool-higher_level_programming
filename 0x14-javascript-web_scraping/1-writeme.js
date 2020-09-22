#!/usr/bin/node
let path = process.argv[2];
const content = process.argv[3];
if (typeof path === 'undefined') {
  path = '';
}
const fs = require('fs');
fs.writeFile(path, content, function (err) {
  if (err) {
    console.log(err);
  }
});
