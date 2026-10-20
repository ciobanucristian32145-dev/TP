# Laborator: funcții, metode și importuri pe web
# Student: <Cristian Ciobanu>

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 
import requests
import urllib.request
from requests import get
import requests as rq
import time
import urllib.parse
import re
import html.parser
import hashlib
import json
import socket
import ssl

#ex35
r = urllib.parse.urlparse("https://cybercor.org/path?x=1#top")
print(r.netloc)
print(r.path)
print(r.query)
print(r.fragment)

#ex 36
print(urllib.parse.urljoin(BASE_URL, "/about"))
print(urllib.parse.urljoin(BASE_URL, "contact.html"))
print(urllib.parse.urljoin(BASE_URL, "../index.html"))

#ex 37
def extract_links(html):
    r = rq.get(html, timeout=TIMEOUT)
    links = re.findall(r'href="([^"]+)"', r.text)
    rezultat = []
    for link in links:
        if link not in rezultat:
            rezultat.append(link)
    print(rezultat)
    return rezultat

# extract_links(BASE_URL)

#ex38
from urllib.parse import urljoin, urlparse

def split_links(links, domain):
    """Returneaza legaturile interne si externe."""
    interne = []
    externe = []
    for link in links:
        url = urljoin(domain, link)
        if urlparse(url).netloc == urlparse(domain).netloc:
            interne.append(url)
        else:
            externe.append(url)
    return interne, externe

links = ["/about", "/contact", "https://httpbin.org"]
interne, externe = split_links(links, BASE_URL)
print("Interne:", interne)
print("Externe:", externe)

#ex39
from html.parser import HTMLParser

class ImageFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            src = dict(attrs).get("src")
            if src is not None:
                self.images.append(src)


# Test pe HTML cunoscut
test_html = """
<html><body>
    <img src="/logo.png" alt="Logo">
    <IMG SRC="poza.jpg">
    <img alt="imagine fara src">
    <img src="https://cdn.example.com/banner.webp" />
    <a href="/despre">Aceasta nu este o imagine</a>
</body></html>
"""

finder = ImageFinder()
finder.feed(test_html)
print(finder.images)

assert finder.images == [
    "/logo.png",
    "poza.jpg",
    "https://cdn.example.com/banner.webp"
], "Parserul nu a gasit imaginile asteptate"

print("Testul a trecut!")

# Test pe pagina reala
r = rq.get(BASE_URL, timeout=TIMEOUT)
finder = ImageFinder()
finder.feed(r.text)

print(len(finder.images), "imagini gasite")
for src in finder.images:
    print(src)

print("Tag-uri img in HTML:", r.text.lower().count("<img"))

# ex 40
def page_fingerprint(url):
    r = rq.get(url, timeout=TIMEOUT)
    return hashlib.sha256(r.content).hexdigest()

a = page_fingerprint(BASE_URL)
time.sleep(1)
b = page_fingerprint(BASE_URL)

print(a)
print(b)
print(a == b)

#ex 41
r = rq.get(BASE_URL, timeout=TIMEOUT)

with open("headers.json", "w", encoding="utf-8") as file:
    json.dump(dict(r.headers), file, indent=2)

with open("headers.json", "r", encoding="utf-8") as file:
    headers = json.load(file)

print(headers.get("Content-Type"))

#ex 42
def resolve(hostname):
    return socket.gethostbyname(hostname)

print(resolve("cybercor.org"))

#ex 43
def cert_days_left(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=TIMEOUT) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as conexiune:
            data = conexiune.getpeercert()["notAfter"]
    expirare = ssl.cert_time_to_seconds(data)
    return int((expirare - time.time()) // 86400)

# print(cert_days_left("cybercor.org"))

