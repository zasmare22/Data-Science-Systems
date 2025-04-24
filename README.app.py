# Capital Time API

IP Address of API: http://35.236.225.8:5000

## How to Use

1. Test if the server is working:

GET http://35.236.225.8:5000/api/hello  
Returns: { "message": "Hello, world!" }

2. Get time info for a capital:

GET http://35.236.225.8:5000/api/time?capital=Tokyo  
Header: Authorization: Bearer supersecrettoken123

Example (curl):
curl -H "Authorization: Bearer supersecrettoken123" "http://35.236.225.8:5000/api/time?capital=Tokyo"
