# Laborator: funcții, metode și importuri pe web
# Student: <Cristian Ciobanu>

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 

import requests as rq
import json
import re
import socket
import ssl
import time
from urllib.parse import urljoin, urlparse
import time
TIMEOUT = 10
DEFAULT_HEADERS = {"User-Agent": "WebLab-Cristian Ciobanu"}

def fetch(url):
    return rq.get(url, headers=DEFAULT_HEADERS, timeout=TIMEOUT)

def get_status(url):
    return fetch(url).status_code

def get_title(html):
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    return html[start:end].strip()

def security_headers(url):
    r = fetch(url)
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
    return rezultat

if __name__ == "__main__":
    print("Autotest:", get_status("https://cybercor.org"))

DEFAULT_HEADERS = {"User-Agent": "WebLab-Cristian Ciobanu"}

#ex 49

def check_paths(base, paths):
    rezultat = {}
    for path in paths:
        rezultat[path] = get_status(base.rstrip("/") + path)
        time.sleep(1)
    return rezultat

#ex 50

def resolve(hostname):
    return socket.gethostbyname(hostname)


def score_headers(results):
    return str(sum(results.values())) + "/" + str(len(results))


def cert_days_left(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=TIMEOUT) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as conexiune:
            data = conexiune.getpeercert()["notAfter"]
    expirare = ssl.cert_time_to_seconds(data)
    return int((expirare - time.time()) // 86400)


def extract_links(html):
    links = re.findall(r'href="([^"]+)"', html)
    rezultat = []
    for link in links:
        if link not in rezultat:
            rezultat.append(link)
    return rezultat


def split_links(links, domain):
    interne = []
    externe = []
    for link in links:
        url = urljoin(domain, link)
        if urlparse(url).scheme in ["http", "https"]:
            if urlparse(url).netloc == urlparse(domain).netloc:
                interne.append(url)
            else:
                externe.append(url)
    return interne, externe


def fetch_robots(base):
    r = fetch(urljoin(base, "/robots.txt"))
    if r.ok:
        return r.text
    return None


def disallowed_paths(robots_text):
    paths = []
    if robots_text is not None:
        for linie in robots_text.splitlines():
            linie = linie.split("#")[0].strip()
            if linie.lower().startswith("disallow:"):
                cale = linie.split(":", 1)[1].strip()
                if cale:
                    paths.append(cale)
    return paths


def site_report(url):
    import json
    from urllib.parse import urlparse

    r = fetch(url)
    titlu = get_title(r.text)
    hostname = urlparse(r.url).hostname
    ip = resolve(hostname)

    time.sleep(1)
    http_url = urlparse(url)._replace(scheme="http").geturl()
    red = fetch(http_url)

    lant = []
    for pas in red.history:
        lant.append(str(pas.status_code))
    lant.append(red.url)
    redirectionari = " -> ".join(lant)

    time.sleep(1)
    scor = score_headers(security_headers(r.url))
    zile = cert_days_left(hostname)

    links = extract_links(r.text)
    interne, externe = split_links(links, r.url)

    time.sleep(1)
    paths = disallowed_paths(fetch_robots(r.url))

    raport = {
        "status": r.status_code,
        "url_final": r.url,
        "titlu": titlu,
        "ip": ip,
        "redirectionari": redirectionari,
        "scor_securitate": scor,
        "zile_certificat": zile,
        "legaturi_interne": len(interne),
        "legaturi_externe": len(externe),
        "cai_interzise": paths
    }

    print("=== Raport site:", url, "===")
    print("Cod de stare:", r.status_code)
    print("URL final:", r.url)
    print("Titlu:", titlu)
    print("Adresa IP:", ip)
    print("Redirectionari:", redirectionari)
    print("Scor securitate:", scor)
    print("Certificat:", zile, "de zile ramase")
    print("Legaturi:", len(interne), "interne,", len(externe), "externe")
    print("Cai interzise:", ", ".join(paths) if paths else "Niciuna")

    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(raport, file, indent=2, ensure_ascii=False)

    print("Salvat in report.json")
    return raport