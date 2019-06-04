const fs = require('fs');
const http = require('http');

const index = 'E:\\Home.html';

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write(fs.readFileSync(index));
  res.end();
}).listen(3000);