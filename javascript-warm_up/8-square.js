#!/usr/bin/node
const args = process.argv.slice(2);
const size = +args[0];

if (Number.isFinite(size) && Number.isInteger(size)) {
  for (let y = 0; y < size; y++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
