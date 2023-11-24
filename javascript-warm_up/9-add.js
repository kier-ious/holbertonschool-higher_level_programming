#!/usr/bin/node

function add(a, b) {
  return a + b;
}
const args = process.argv.slice(2);
const num1 = +args[0];
const num2 = +args[1];

if (Number.isFinite(num1) && Number.isInteger(num2)) {
  const result = add(num1, num2);
  console.log(result);
} else {
  console.log('NaN');
}
