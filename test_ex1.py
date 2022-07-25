import socket
import sys
import requests

KILOBYTE = 1024
SERVER_ADDRESS = "http://localhost:8080/"

param_d = {"subfilepath":"test.html"}
r = requests.get(SERVER_ADDRESS,params=param_d)



print(f"client received {(r.headers)} bytes: '{str(r.content, 'utf-8')}'")
