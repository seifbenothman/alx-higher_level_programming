#!/usr/bin/node
const arg = process.argv[2];
const convertNumber = parseInt(arg);
if (isNaN(convertNumber) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convertNumber);
}