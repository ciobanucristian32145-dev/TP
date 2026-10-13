import requests

SITES = [
    # Pagini obișnuite (Părțile 2, 3 și 4)
    "https://example.com",
    "https://httpbin.org/html",
    "https://httpbin.org/json",
    "https://httpbin.org/status/200",
    "https://httpbin.org/redirect/1",
    "https://httpbin.org/delay/2",
    # Pagini care eșuează
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
    "https://httpbin.org/delay/10",
    "http://this-site-does-not-exist.invalid",
    # Anteturi de securitate (Partea 5)
    "https://httpbin.org/response-headers?X-Frame-Options=DENY&X-Content-Type-Options=nosniff",
    "https://httpbin.org/response-headers?x-frame-options=DENY",
    # Răspunde aleatoriu cu 200 sau 500 (Partea 6)
    "https://httpbin.org/status/200,500",
]

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
]


def build_url(host, path):
    """Returnează o adresă completă, de exemplu https://example.com/login."""
    return "https://" + host + "/" + path.lstrip("/")


def is_https(url):
    """Returnează True dacă adresa începe cu https://, altfel False."""
    return url.startswith("https://")

# Teste pentru build_url
print(build_url("example.com", "login"))
print(build_url("example.com", "/login"))

# Teste pentru is_https
print(is_https(SITES[0]))
print(is_https(SITES[9]))


def show_response(url):
    """Trimite un GET la url și afișează statusul și Content-Type."""
    r = requests.get(url)
    print("Status:", r.status_code)
    print("Content-Type:", r.headers.get("Content-Type"))

# Test
show_response("https://example.com")


def check_site(url):
    """Returnează un dicționar cu: status, content_type, length, server."""
    try:
        r = requests.get(url, timeout=5)

        return {
            "status": r.status_code,
            "content_type": r.headers.get("Content-Type", "unknown"),
            "length": len(r.content),
            "server": r.headers.get("Server", "unknown")
        }

    except requests.exceptions.RequestException as e:
        return {"status": None, "error": str(e)[:100]}


# Testam toate site-urile
for site in SITES:
    print(site)
    print(check_site(site))
    print()


def scan_sites():
    """Verifică toate site-urile din SITES, afișează-le pe cele care merg și un rezumat."""
    rezultate = []
    for site in SITES:
        rezultat = check_site(site)
        rezultate.append((site, rezultat))
    reusite = []
    for site, rezultat in rezultate:
        if rezultat["status"] == 200:
            reusite.append((site, rezultat))
    reusite.sort(key=lambda x: x[1]["length"], reverse=True)
    for site, rezultat in reusite:
        print(site, "->", rezultat["status"], ",", rezultat["length"], "octeți")
    print("Reușite:", len(reusite), "| Eșuate:", len(rezultate) - len(reusite))

# Test
scan_sites()

def check_headers(url):
    """Returnează un dicționar cu: present, missing, score."""
    present = []
    missing = []

    try:
        r = requests.get(url, timeout=5)

        for header in SECURITY_HEADERS:
            if header in r.headers:
                present.append(header)
            else:
                missing.append(header)
        return {
            "present": present,
            "missing": missing,
            "score": len(present)
        }

    except requests.exceptions.RequestException:
        return {
            "present": [],
            "missing": SECURITY_HEADERS.copy(),
            "score": 0
        }


# Teste
print(check_headers(SITES[10]))
print(check_headers(SITES[11]))


def retry_check(url, attempts=3):
    """Încearcă de cel mult `attempts` ori; returnează un dicționar cu: status, attempts."""
    status = None
    error = None
    erori = 0
    nr_incercari = 0

    for i in range(attempts):
        nr_incercari += 1
        try:
            r = requests.get(url, timeout=5)
            status = r.status_code
            if status < 500:
                return {"status": status, "attempts": nr_incercari}

        except requests.exceptions.RequestException as e:
            error = str(e)
            erori += 1
    rezultat = {"status": status, "attempts": nr_incercari}

    if erori == nr_incercari and nr_incercari > 0:
        rezultat["error"] = error
    return rezultat


# Teste
print(retry_check("https://httpbin.org/status/200"))
print(retry_check("https://httpbin.org/status/404"))
print(retry_check("https://httpbin.org/status/500"))
print(retry_check("https://httpbin.org/status/500", attempts=2))
print(retry_check("http://this-site-does-not-exist.invalid"))