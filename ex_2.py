"""
Exercise 2
Read the documentation for the requests library to see how to post 
data to a server (i.e., how to upload a file) and then (a) write a program 
that uploads a CSV file using POST and (b) modify the server to accept an 
uploaded CSV file and return an HTML page that displays that CSV as a table 
in an HTML page.
"""

# This program uploads a csv file
import requests

upload_csv = "test_upload.csv"

url = 'http://localhost:8080'

files = {'upload_csv':open(upload_csv,'rb')}
fileval = {'OUT': 'csv'}

x = requests.post(url, files=files, data=fileval)

print(x.text)


