from urllib import request

response = request.urlopen("http://www.biquge.cc")
print(response.read())
