import http.server

BODY = "***filecontents***"
conn = http.client.HTTPConnection("10.129.2.148", 8081)
conn.request("PUT", "C:\\Users\\paula\\Desktop\\client.py", BODY)
response = conn.getresponse()
print(response.status, response.reason)

#test