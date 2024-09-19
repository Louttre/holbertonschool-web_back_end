const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();

app.use((req, res, next) => {
  res.setHeader('Content-Type', 'text/plain');
  next();
});

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const csvFilePath = path.resolve(__dirname, 'students.csv');
  fs.readFile(csvFilePath, 'utf8', (err, data) => {
    if (err) {
      res.status(500).send('Unable to read the file');
      return;
    }

    const lines = data.trim().split('\n').filter(line => line.trim() !== '');
    const students = lines.join('\n');

    res.send(`This is the list of our students\n${students}`);
  });
});

app.listen(1245);

module.exports = app;
