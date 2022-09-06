#!/usr/bin/node

const cmdArgs = parseInt(process.argv[2]);

if (Number.isNaN(cmdArgs)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + cmdArgs);
}
