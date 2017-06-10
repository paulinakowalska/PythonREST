import http.client
BODY = "***filecontents***"
conn = http.client.HTTPConnection("192.168.0.3", 8081)
# conn.request("PUT", "C:\\Users\\paula\\Desktop\\client.py", BODY)
conn.request("GET", "/")
response = conn.getresponse()
print(response.status, response.reason, response.read())
