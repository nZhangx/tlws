"""
Exercise 1: 
Modify the server so that it reads HTML pages from disk and returns them. 
For example, if the client requests about.html, the server should read 
the page ./about.html and return that content.

"""

from http.server import HTTPServer, BaseHTTPRequestHandler

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
        if not(filepath is None):
            output = bytes(PAGE)
        else:
            # get files availabled
            file_map = server.file_map
            # make sure the page exists
            assert self.path in file_map, "file {} not found".format(self.path)
            # read file
            output = bytes(self.readfile_local(self.path))
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Returning page", str(self.path))
        self.end_headers()
        self.wfile.write(output)


if __name__ == "__main__":
    server = ("", 8080)
    server = HTTPServer(server, RequestHandler)
    server.serve_forever()
