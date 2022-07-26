"""
Exercise 1: 
Modify the server so that it reads HTML pages from disk and returns them. 
For example, if the client requests about.html, the server should read 
the page ./about.html and return that content.

"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import os
from urllib.parse import urlparse
import pandas as pd
from urlparse import parse_qs
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
            compile_str = ""
            flines = readfile.readlines()
            for line in flines:
                compile_str += line
        return compile_str

    # Handle a GET request.
    def do_GET(self):
        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        if not('filepath' in query_components):
            output = bytes(PAGE, "utf-8")
        else:
            assert os.path.exists(query_components['filepath']), "file {} not found".format(query_components['filepath'])
            # read file
            output = bytes(self.readfile_local(query_components['filepath']), "utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Returning page", str(self.path))
        self.end_headers()
        self.wfile.write(output)

    # Handle a POST request
    def do_POST(self):
        # use cgi library:
        #   can be uploading terabytes. 
        #   This is why we need to read in chunk
        #   tell you what to expect
        #   will break if upload huge datafile (common hacker trick)
        # take in a csv and 
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # can include encoding in header too (ex. east asian datasets - encodings)
        content_len = int(self.headers.get('content-length', 0))
        post_body = (self.rfile.read(content_len)).decode("utf-8") 
        post_df = pd.read_csv(post_body)
        df_html = post_df.to_html()
        self.wfile.write("received post request:<br>{}".format(df_html))


if __name__ == "__main__":
    server = ("", 8080)
    server = HTTPServer(server, RequestHandler)
    server.serve_forever()

"""
Now it's about authentication.
Unsolvable problem in theory - ANy ID can be spoofed in theory but needs effort
Biggest leak: search history (used against in court)
"""