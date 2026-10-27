# Laborator: funcții, metode și importuri pe web
# Student: <Cristian Ciobanu>

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  
from webtools import get_title, security_headers, get_status
import webtools
import requests as rq
# #ex 44
print(webtools.get_title(webtools.fetch(BASE_URL).text))

# #ex 45
r = rq.get(BASE_URL, timeout=10)
print(get_title(r.text))

# #ex 46
if __name__ == "__main__":
   print("Autotest:", get_status("https://cybercor.org"))

# #ex 47
from webtools import DEFAULT_HEADERS

print(DEFAULT_HEADERS)

# # ex 48
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()

r = webtools.fetch(args.url)
print(webtools.get_title(r.text))

#ex 49
import csv
from datetime import datetime

paths = ["/", "/robots.txt", "/sitemap.xml"]
rezultat = webtools.check_paths(args.url, paths)

with open("report.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["path", "status", "checked_at"])

    for path, status in rezultat.items():
        writer.writerow([path, status, datetime.now().isoformat()])

print("Salvat in report.csv")

# #ex 50
webtools.site_report(args.url)
