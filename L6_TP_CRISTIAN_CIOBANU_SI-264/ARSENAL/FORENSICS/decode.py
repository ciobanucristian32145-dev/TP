import re
import base64
from urllib.parse import unquote
import hashlib 
import argparse, json
# #A1
s = "Salut"
b = s.encode()          # bytes
print(b, b[0])          # b"Salut" 83
h = b.hex()
print(h)
print(bytes.fromhex(h))

# #A2
def ghici_strat(s):
    if "%" in s:
        return "url"
    if len(s) % 2 == 0 and re.fullmatch(r"[0-9a-fA-F]+", s):
        return "hex"
    if re.fullmatch(r"[A-Za-z0-9+/=]+", s):
        return "base64"
    return "necunoscut"
print(ghici_strat("%2Fetc"))   # url
print(ghici_strat("48656c6c6f"))  # hex

#A3
def desfa(s):
    strat = ghici_strat(s)
    if strat == "base64":
        return strat, base64.b64decode(s)
    if strat == "hex":
        return strat, bytes.fromhex(s)
    if strat == "url":
        return strat, unquote(s).encode()
    return strat, s.encode()

#A4
def citibil(b):
    return all(32 <= c < 127 for c in b)
 
val = "NTM1OTU3NTk="
for _ in range(8):
    strat, b = desfa(val)
    if citibil(b):
        print(b.decode())
        break
    else:
        val = b.decode()


#A5
date = open("probe/xor.bin", "rb").read()
for k in range(256):
    clar = bytes(b ^ k for b in date)
    if citibil(clar):
       print("cheie:", k, clar.decode())
       break

#A6
tinta = open("probe/hashuri.txt").readline().strip()
print(len(tinta))   # 32 md5 / 40 sha1 / 64 sha256
for cuv in open("probe/wordlist.txt", encoding="latin1"):
    cuv = cuv.strip()
    if hashlib.md5(cuv.encode()).hexdigest() == tinta:
         print("gasit:", cuv)
         break

#A7
if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("intrare")          # sir sau cale
    p.add_argument("--fisier", action="store_true")
    a = p.parse_args()

    if a.fisier:
        s = open(a.intrare, "rb").read().decode().strip()
    else:
        s = a.intrare

    strat, b = desfa(s)

    fisa = {"strat": strat, "rezultat": b.decode()}
    json.dump(fisa, open("FORENSICS/fisa.json", "w"))