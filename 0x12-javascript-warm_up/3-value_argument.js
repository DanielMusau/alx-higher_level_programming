#!/usr/bin/node

const cmdArgs = process.argv;

if (cmdArgs[2] === undefined) {
  console.log('No argument');
} else {
  console.log(cmdArgs[2]);
}
