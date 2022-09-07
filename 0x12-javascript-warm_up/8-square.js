#!/usr/bin/node

const cmdArgs = parseInt(process.argv[2]);

if (Number.isNaN(cmdArgs)) {
  console.log('Missing size');
} else {
  for (let i = 0, s; i < cmdArgs; i++) {
    s = '';
    for (let j = 0; j < cmdArgs; j++) {
      s += 'X';
    }
    console.log(s);
  }
}
