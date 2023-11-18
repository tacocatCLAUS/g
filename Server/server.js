const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
  if (req.method === 'POST') {
    let body = '';

    req.on('data', (chunk) => {
      body += chunk;
    });

    req.on('end', () => {
      // Check for the special request to clear the file
      if (req.url === '/clear') {
        clearFile(res);
      } else {
        // Append the posted data to the file with a newline character
        fs.appendFile('posted_data.txt', body + '\n', (err) => {
          if (err) {
            res.writeHead(500, { 'Content-Type': 'text/plain' });
            res.end('Internal Server Error');
            console.error(err);
          } else {
            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end('Data saved successfully');
          }
        });
      }
    });
  } else if (req.method === 'GET' || req.connection.encrypted) {
    // Retrieve the posted data from the file (you can modify this as needed)
    fs.readFile('posted_data.txt', 'utf8', (err, data) => {
      if (err) {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('Internal Server Error');
        console.error(err);
      } else {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(data || 'Hello I love Snakes. You must type.');
      }
    });
  } else {
    // For non-HTTPS and non-GET requests, respond with a blank page
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end('<html><head></head><body></body></html>');
  }
});

const clearFile = (res) => {
  // Clear the file by overwriting it with an empty string
  fs.writeFile('posted_data.txt', '', (err) => {
    if (err) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('Internal Server Error');
      console.error(err);
    } else {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end('File cleared successfully');
    }
  });
};

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
