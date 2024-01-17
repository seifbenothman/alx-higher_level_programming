#!/usr/bin/node

const arg = process.argv.slice(2);
let secondMax = 0;

if (arg.length > 1) {
  const integers = arg.map(Number);
  integers.sort((a, b) => b - a);
  secondMax = integers[1];
}

console.log(secondMax);