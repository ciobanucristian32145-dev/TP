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

def get_status(url):
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code

#ex21
def fetch(url, timeout=10):
    return rq.get(url, timeout=TIMEOUT)
# r = fetch(BASE_URL)
# print(r.status_code)

#ex22
# print(get_status(BASE_URL + "/"))
# time.sleep(1)
# print(get_status(BASE_URL + "/robots.txt"))
# time.sleep(1)
# print(get_status(BASE_URL + "/sitemap.xml"))

#ex23
# print(fetch(BASE_URL, timeout=3))
# print(fetch(BASE_URL))

#ex24
def get_title(html):
    r = rq.get(html, timeout=TIMEOUT)
    html = r.text
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    titlu = html[start:end].strip()
    print(titlu)
# get_title(BASE_URL)

#ex 25
def get_title(html):
    """extrage si afiseaza titlul unei pagini html din <title></title>
    html este argumentul string ce reprezinta 
    continutul paginii ca un sir de caractere"""
    r = rq.get(html, timeout=TIMEOUT)
    html = r.text
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    titlu = html[start:end].strip()
    print(titlu)
# help(get_title)

#ex 26
def get_status(url: str) -> int:
    r = rq.get(url, timeout=TIMEOUT)
    return r.status_code

# print(get_status(123))

#ex27
def page_exists(url):
    try:
        r = rq.get(url, timeout=TIMEOUT)
        return r.ok
    except rq.RequestException:
        return False
print(page_exists(BASE_URL))
print(page_exists("https://this-domain-does-not-exist.invalid"))

#ex28
def check_paths(base, paths):
    rezultat = {}
    for path in paths:
        rezultat[path] = get_status(base + path)
        time.sleep(1)
    print(rezultat)
    return rezultat

# paths = ["/", "/robots.txt", "/sitemap.xml"]
# check_paths(BASE_URL, paths)

#ex29
def get_header(url, name, default="lipseste"):
    r = rq.get(url, timeout=TIMEOUT)
    return r.headers.get(name, default)
# print(get_header(BASE_URL, name="Server"))

#ex 30
def security_headers(url):
    r = rq.get(url, timeout=TIMEOUT)
    antete = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy"
    ]
    rezultat = {}
    for antet in antete:
        rezultat[antet] = antet in r.headers
    print(rezultat)
    return rezultat

# security_headers(BASE_URL)

#ex 31
def score_headers(results):
    n = 0
    for valoare in results.values():
        if valoare:
            n += 1
    scor = str(n) + "/" + str(len(results))
    print(scor)
    return scor

# score_headers(security_headers(BASE_URL))

#ex32
def fetch_robots(base):
    r = rq.get(base + "/robots.txt", timeout=TIMEOUT)
    if r.ok:
        return r.text
    return None


def disallowed_paths(robots_text):
    paths = []
    if robots_text is not None:
        for linie in robots_text.splitlines():
            if linie.startswith("Disallow:"):
                cale = linie.split(":", 1)[1].strip()
                if cale:
                    paths.append(cale)
    print(paths)
    return paths


# disallowed_paths(fetch_robots(BASE_URL))

#ex 33
def response_times(*urls):
    rezultat = {}
    for url in urls:
        start = time.perf_counter()
        r = rq.get(url, timeout=TIMEOUT)
        rezultat[url] = time.perf_counter() - start
        time.sleep(1)
    print(rezultat)
    return rezultat

# response_times(BASE_URL, BASE_URL + "/robots.txt")

#ex 34
def log(message, **details):
    print(message, end="")
    for nume, valoare in details.items():
        print(f" | {nume}={valoare}", end="")
    print()

log("verificat", url=BASE_URL, status=200)

