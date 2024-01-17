#!/usr/bin/node
const arg = process.argv[2];
function Factorial (arg) {
  if (isNaN(arg) === true || arg === 1) {
    return (1);
  } else {
    return (arg * Factorial(arg - 1));
  }
}
console.log(Factorial(parseInt(arg)));