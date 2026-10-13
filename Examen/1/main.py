import requests
from checker import (
    build_url, is_https, show_response,
    check_site, scan_sites, check_headers, retry_check
)

# Partea 1
print("Partea 1 - build_url:")
print(build_url("example.com", "login"))
print(build_url("example.com", "/login"))

print("Partea 1 - is_https:")
print(is_https("https://example.com"))
print(is_https("http://example.com"))


# Partea 2
print("\nPartea 2 - show_response:")

try:
    print("Site normal:")
    show_response("https://example.com")

    print("Site cu eroare 404:")
    show_response("https://httpbin.org/status/404")

except requests.exceptions.RequestException as e:
    print("Eroare:", e)


# Partea 3
print("\nPartea 3 - check_site:")
print("Site valid:", check_site("https://example.com"))
print("Site invalid:", check_site("http://this-site-does-not-exist.invalid"))


# Partea 4
print("\nPartea 4 - scan_sites:")
scan_sites()


# Partea 5
print("\nPartea 5 - check_headers:")
print("Site cu anteturi:", check_headers(
    "https://httpbin.org/response-headers?X-Frame-Options=DENY&X-Content-Type-Options=nosniff"
))

print("Site invalid:", check_headers(
    "http://this-site-does-not-exist.invalid"
))


# Partea 6
print("\nPartea 6 - retry_check:")
print("Status 200:", retry_check("https://httpbin.org/status/200"))
print("Status 404:", retry_check("https://httpbin.org/status/404"))
print("Status 500:", retry_check("https://httpbin.org/status/500"))