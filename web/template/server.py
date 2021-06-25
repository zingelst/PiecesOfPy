import sys
from urllib.parse import urlparse,parse_qs

from http.server import BaseHTTPRequestHandler,HTTPServer
from mako.template import Template
from mako import exceptions

PORT_NUMBER = 8000

class MyHandler(BaseHTTPRequestHandler):
    """This class will handles any incoming request from
    the browser. Any method defined as do_<NAME> willhandle
    that type of HTTP request.
    """
    def send_headers(self):
        """Use before you send any data back via the wfile
        """
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

    def do_GET(self):
        """Handler for GET requests"""
        self.send_headers()
        # Requestline is GET <url> HTTP/1.0, so just grab the middle request
        req = self.requestline.split(' ')[1]
        url = urlparse(req)
        query = parse_qs(url.query)

        if url.path == "/":
            self.handle_index(url, query)
        else:
            # Dunno
            content = url.path
            self.wfile.write(content.encode('utf-8'))
    
    def handle_index(self, url, query):
        """Render the index template"""
        try:
            # Can do some data here if you want
            template = Template(filename="index_template.html").render()
            self.wfile.write(template.encode('utf-8'))
        except:
            self.wfile.write(exceptions.html_error_template().render())

    def do_POST(self):
        """Handler for POST requests"""
        self.send_headers()
        # Get the size of the data
        content_length = int(self.headers['Content-Length'])
        # Get the data contained in the POST request
        post_data = self.rfile.read(content_length)
        # This dumps whatever POST reques came in to the console
        print(f"POST: Path: {self.path} Data: [{post_data}]")

        # Send a response back to the client, simple "OK" is all
        resp = "OK"
        self.wfile.write(resp.encode('utf-8'))


def main():
    try:
        # Creates an HTTP Server that will listen on all interface (0.0.0.0)
        # on PORT_NUMBER (defined above as 9012) and all of the requests will
        # be handled by the MyHandler class defined above.
        server = HTTPServer(('0.0.0.0', PORT_NUMBER), MyHandler)
        print('Started httpserver on port ' , PORT_NUMBER)

        #Wait forever for incoming htto requests
        server.serve_forever()

    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        server.socket.close()

if __name__ == "__main__":
    main()
