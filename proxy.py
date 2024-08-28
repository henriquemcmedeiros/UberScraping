import http.server
import socketserver
import urllib.request

class ProxyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:]  
        if not url:
            self.send_response(400)
            self.end_headers()
            return

        try:
            with urllib.request.urlopen(url) as response:
                self.send_response(response.getcode())
                self.send_header('Content-Type', response.headers.get('Content-Type'))
                self.end_headers()
                self.wfile.write(response.read())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(f"Error: {e}".encode())

def run(server_class=http.server.HTTPServer, handler_class=ProxyHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting proxy server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
