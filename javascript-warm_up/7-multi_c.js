#!/usr/bin/node

const x = parseInt(process.argv);
let i = 0;

if (isNaN(x)) {
  console.log("Missing number of occurrences");
} else {
  while (i < x) {
    console.log("C is fun");
    i++;
  }
}
