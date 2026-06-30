const http = require("http");

const port = process.env.PORT || 8080;

const server = http.createServer((request, response) => {
  response.writeHead(200, { "Content-Type": "text/plain" });
  response.end("Hello from Node.js");
});

server.listen(port, "0.0.0.0", () => {
  console.log(`Listening on http://localhost:${port}`);
});
