#!/usr/bin/node

const cmdArgs = parseInt(process.argv[2]);

if (Number.isNaN(cmdArgs)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= cmdArgs; i++) {
    console.log('C is fun');
  }
}
