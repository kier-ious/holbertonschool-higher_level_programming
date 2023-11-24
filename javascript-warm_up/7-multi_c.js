#!/usr/bin/node
const args = process.argv.slice(2);
const noo = +args[0];

if (Number.isFinite(noo) && Number.isInteger(noo)) {
  for (let y = 0; y < noo; y++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number if occurrences');
}
