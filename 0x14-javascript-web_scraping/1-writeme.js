#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const string = process.argv[3];

fs.writeFile(filePath, string, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
