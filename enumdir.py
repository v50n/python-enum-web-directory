import http.client

print("---this program will try to get a specific directory in any webserver---")
host = input("Insert here the host/IP: ")
port = int(input("the port: "))
dir = input("What directory you want to verify ? : ")

if port == "":
    port = 80

try: 
    connection = http.client.HTTPConnection(host,port)
    connection.request('GET','/%s' % dir)
    response = connection.getresponse()
    if response.status == 200:
        print("the web have the directory: /" dir)
    else:
        print("Not found :/",dir)
    connection.close()
except ConnectionRefusedError:
    print("connection failed")
