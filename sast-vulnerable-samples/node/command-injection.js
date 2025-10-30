const { exec } = require('child_process');

function runSearch(userInput) {
  // Command injection: user input is concatenated into a shell command
  exec('grep -R "' + userInput + '" ./', (err, stdout, stderr) => {
    if (stdout) console.log(stdout);
    if (stderr) console.error(stderr);
  });
}

const arg = process.argv[2];
if (arg) {
  runSearch(arg);
}


