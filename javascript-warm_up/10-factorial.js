#!/usr/bin/node

function factorial (n) {
  // base case, factorial of 0 is 1
  if (isNaN(n) || n < 0) {
    return 1;
  }
  // recusive case, n! = n* (n-1)!
  return n * factorial(n - 1);
}

const args = process.argv.slice(2);
const input = parseInt(args[0], 10);

if(isNaN(input)) {
  console.log('NaN');
} else {
  console.log(factorial(input));
}
