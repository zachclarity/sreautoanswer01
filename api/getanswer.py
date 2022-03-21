from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
import logging

class handler(BaseHTTPRequestHandler):
  def do_POST(self):
    content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
    post_data = self.rfile.read(content_length) # <--- Gets the data itself
    #logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
    #    str(self.path), str(self.headers), post_data.decode('utf-8'))

    self._set_response()
    self.wfile.write("POST request for {}".format(post_data).encode('utf-8'))
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    answer = "auto answer v0.1 Beta "
    self.wfile.write("Works: {}:".format(answer).encode('utf-8'))
    return

def run(server_class=HTTPServer, handler_class=handler, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()