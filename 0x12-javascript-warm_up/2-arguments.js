#!/usr/bin/node

const cmdArgs = process.argv;

if (cmdArgs.length === 2) {
  console.log('No argument');
} else if (cmdArgs.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
