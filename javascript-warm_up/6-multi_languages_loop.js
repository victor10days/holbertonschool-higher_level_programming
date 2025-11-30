#!/usr/bin/node

const lines = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let output = '';

for (const line of lines) {
  output += line + '\n';
}

console.log(output.slice(0, -1));
