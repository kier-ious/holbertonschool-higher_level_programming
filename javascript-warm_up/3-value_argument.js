#!/usr/local/bin/node
const args = process.argv.slice(2);
const firstArgument = args[0];

if (firstArgument === undefined) {
  console.log('No argument');
} else {
  console.log(firstArgument);
}
