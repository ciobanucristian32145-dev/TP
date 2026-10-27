from PIL import Image
# #B5
img = Image.open("probe/foto.jpg").convert("RGB")
px = list(img.getdata())
mesaj = b"FLAG{ascuns_in_pixeli}"
biti = "".join(f"{x:08b}" for x in mesaj)
px_nou = []
idx_bit = 0
total_biti = len(biti)

for r, g, b in px:
    canale = [r, g, b]
    for i in range(3):
        if idx_bit < total_biti:
            canale[i] = (canale[i] & ~1) | int(biti[idx_bit])
            idx_bit += 1
    px_nou.append(tuple(canale))

img.putdata(px_nou)
img.save("stego.png")

#B6
px = list(Image.open("stego.png").convert("RGB").get_flattened_data())
biti = ""

for r, g, b in px:
    biti += str(r & 1)
    biti += str(g & 1)
    biti += str(b & 1)

mesaj = bytearray()
for i in range(0, len(biti), 8):
    octet = int(biti[i:i+8], 2)
    if octet == 0:
        break
    mesaj.append(octet)

print(mesaj[:22].decode())

# Pentru varful salii
import base64
date = open("probe/challenge.bin", "rb").read().strip()
date = base64.b64decode(date)
for k in range(256):
    clar = bytes(b ^ k for b in date)
    if b"FLAG{" in clar:
        print("cheie:", k)
        print("mesaj:", clar.decode())
