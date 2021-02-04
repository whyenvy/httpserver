#!/usr/bin/env python3
"""
Made by envy#0449
Simple Python HTTP Server.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import pyfiglet

print("[+] Made by envy#0449")
print("[+] Github : https://github.com/whyenvy")

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>HTTP Server - envy#0449</title></head>", "utf-8"))
        self.wfile.write(bytes("<big>Server Testing</big>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>HTTp-server</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")