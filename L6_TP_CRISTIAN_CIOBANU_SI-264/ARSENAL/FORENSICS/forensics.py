import re
from PIL import Image
from PIL.ExifTags import TAGS

#B1
def tip_real(cale):
    cap = open(cale, "rb").read(8)
    if cap.startswith(b"%PDF"):
        return "pdf"
    if cap.startswith(b"\x89PNG"):
        return "png"
    if cap.startswith(b"\xff\xd8"):
        return "jpeg"
    if cap.startswith(b"PK\x03\x04"):
        return "zip/docx"
    return cap.hex()
print(tip_real("probe/foto.jpg"))

#B2
date = open("probe/ascuns.png", "rb").read()
for m in re.findall(rb"[ -~]{4,}", date):
 print(m.decode())
# cauta un indiciu: o cale, un mesaj, un nume de fisier

#B3
exif = Image.open("probe/foto.jpg")._getexif() or {}
for id, val in exif.items():
    print(TAGS.get(id, id), "=", val)

gps = exif[34853]
lat = float(gps[2][0]) + float(gps[2][1]) / 60 + float(gps[2][2]) / 3600
lon = float(gps[4][0]) + float(gps[4][1]) / 60 + float(gps[4][2]) / 3600
print(f"GPS: {lat:.6f}, {lon:.6f}")

#B4
date = open("probe/ascuns.png", "rb").read()
i = date.find(b"PK\x03\x04")
if i != -1:
 open("gasit.zip","wb").write(date[i:])
 print("arhiva extrasa de la octetul", i)
 for m in re.findall(rb"[ -~]{4,}", date[i:]):
        print(m.decode())