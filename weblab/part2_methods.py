# Laborator: funcții, metode și importuri pe web
# Student: <Cristian Ciobanu>

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import requests
import urllib.request
from requests import get
import requests as rq
import time
# #ex9
# r = rq.get(BASE_URL, timeout=TIMEOUT)
# print(r.status_code)
# print(r.ok)
# print(r.url)
# print(r.encoding)

# #ex10
# r = rq.get(BASE_URL, timeout=TIMEOUT)
# r.raise_for_status() 
# try:
#     r2 = requests.get(BASE_URL + "/this-page-does-not-exist", timeout=TIMEOUT)
#     r2.raise_for_status()
# except requests.HTTPError:
#     print("Atenție: Pagina căutată nu există!")

# #ex11
# r = rq.get(BASE_URL, timeout=TIMEOUT)
# for nume,valoare in r.headers.items():
#     print(f"{nume}: {valoare}")

# #ex12
# r = rq.get(BASE_URL, timeout=TIMEOUT)
# server = r.headers.get("Server","Lipseste")
# ct = r.headers.get("Content-type","Lipseste")
# print("server", server)
# print("content-type",ct)
# content_type_lower = r.headers.get("content-type", "lipsește")
# print("content-type (cu litere mici):", content_type_lower)

# #ex13
# r = rq.get(BASE_URL, timeout=TIMEOUT)
# cyber = r.text.lower().count("cyber")
# print(cyber)

# #ex14
# r = rq.get(BASE_URL, timeout=TIMEOUT)
# html = r.text
# start = html.find("<title>") + len("<title>")
# end = html.find("</title>")
# titlu = html[start:end].strip()
# print(titlu)

# #ex15
# r = rq.get(BASE_URL, timeout=TIMEOUT)
# html = r.text.splitlines()
# print(len(html))
# linie_lunga = max(html, key=len)
# print("cea mai lunga linie", linie_lunga)

# #ex16
# r = rq.get(BASE_URL, timeout=TIMEOUT)
# if r.url.startswith("https://"):
#     print("Conexiune sec")
# else:
#     print("Conexiune nesecurizata")

# #ex17
# r = rq.get("http://cybercor.org", timeout=TIMEOUT)
# for resp in r.history:
#   d = resp.headers.get("Location")
#   print(f"{resp.status_code}: {resp.url} -> {d}")
# print("destinatia finala:", r.url)

# #ex18
# rg = rq.get(BASE_URL, timeout=TIMEOUT)
# rh = rq.head(BASE_URL, timeout=TIMEOUT)
# print("cu rq head:" ,len(rh.content))
# print("cu rq get:" ,len(rg.content))

# #ex19
# r = rq.get(BASE_URL, timeout=TIMEOUT)
# if r.cookies:
#     for cookie in r.cookies:
#         print(f"Nume:{cookie.name} Este securizat?:{cookie.secure}")
# else:
#     print("nici un cookie setat")

# #ex20
# session = rq.Session()
# session.headers.update({"User-Agent": "WebLab-<Cristian Ciobanu>"})
# r = session.get(ECHO_URL + "/headers")
# print(r.text)
# print(r.json)