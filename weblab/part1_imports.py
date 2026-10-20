# Laborator: funcții, metode și importuri pe web
# Student: <Cristian Ciobanu>

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

#ex.1
# import requests
# print(requests.__version__)
# import urllib.request
# #requests se instalează separat, iar urllib vine deja cu Python. Programul afișează versiunea lui requests

# #ex2
# from requests import get
# r1 = requests.get(BASE_URL)
# print(r1.status_code)
# r2 = get(BASE_URL)
# print(r2.status_code)

# #ex3
# import requests as rq
# rq.get(BASE_URL)
# #ex4

# r=urllib.request.urlopen(ECHO_URL)
# print(r.status)
# b = r.read().decode("utf-8")
# print(b[:200])

# #ex5
# print(dir(requests))


# #ex6
# help(requests.get)
# r = rq.get(BASE_URL, timeout=TIMEOUT)
# print(r.status_code)

# # #ex7
# import time
# s = time.perf_counter()
# r = rq.get(BASE_URL, timeout=TIMEOUT)
# e = time.perf_counter()
# print(e - s)

# #ex8
try:
  import base64
  print("este deja")
except ImportError:
    print("instaleaza modulul")
