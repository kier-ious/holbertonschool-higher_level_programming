#!/usr/bin/node
const arg = process.argv[2];

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
if (parseInt(arg)) {
  console.log(factorial(arg));
} else console.log(1);
