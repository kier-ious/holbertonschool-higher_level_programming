#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
try {
  console.log('File content:\n', fs.readFileSync(filePath, 'utf-8'));
} catch (err) {
  console.error('Error reading the file:', err);
}
