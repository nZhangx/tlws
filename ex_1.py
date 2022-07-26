"""
Exercise 1: 
Modify the server so that it reads HTML pages from disk and returns them. 
For example, if the client requests about.html, the server should read 
the page ./about.html and return that content.

"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import os
# Page to send back.
PAGE = """\
<html>
<body>
<p>Hello, web!</p>
</body>
</html>
"""

class RequestHandler(BaseHTTPRequestHandler):
    """Handle HTTP requests by returning a fixed "page"."""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args,**kwargs)

    def readfile_local(self,path):
        with open(path,'r') as readfile:
            flines = readfile.readlines()
        return flines

    # Handle a GET request.
    def do_GET(self,filepath=None):
        if not (self.path is None):
            output = bytes(PAGE, "utf-8")
        else:
            assert os.path.exists(filepath), "file {} not found".format(filepath)
            # read file
            output = bytes(self.readfile_local(self.path), "utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Returning page", str(self.path))
        self.end_headers()
        self.wfile.write(output)


if __name__ == "__main__":
    server = ("", 8080)
    server = HTTPServer(server, RequestHandler)
    server.serve_forever()
