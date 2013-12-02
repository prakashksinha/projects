var http=require("http");
var server=http.createServer(onRequest);
server.listen(8888);
function onRequest(request, response) {
    console.log("Request received");
    response.writeHead(200, {"Content-Type": "text/plain"});
    response.write("Hello World");
    response.end();
}
console.log("Server has started");
