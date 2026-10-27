# Raport de laborator 6

**Student:** Ciobanu Cristian  
**Grupa:** SI-264  
**Tema:** Informații invizibile, forensics și steganografie

## Lucrarea A

- **Mesajul cu straturi:** `FLAG{straturi_de_encoding}`. L-am obținut prin decodare Base64 → Base64 → hex.
- **Cheia XOR:** `128` (`0x80`). Mesajul recuperat este `Un singur octet tine tot secretul... gaseste-l! FLAG{xor_un_octet}`.
- **Parola găsită:** `password`, prin compararea cuvintelor din dicționar cu hash-ul MD5 `5f4dcc3b5aa765d61d8327deb882cf99`.

## Lucrarea B

- **Tipurile reale:** `foto.jpg` — JPEG; `ascuns.png` și `stego.png` — PNG; `gasit.zip` — arhivă ZIP. Tipurile au fost verificate după semnăturile fișierelor.
- **Metadatele din foto.jpg:** producător `Apple`, model `iPhone 13`, data și ora `2026:09:14 10:30:00`.
- **GPS:** `47° 1′ 0″ N`, `28° 51′ 27″ E`, adică **47.016667, 28.857500** în grade zecimale.
- **Arhiva ascunsă:** în `ascuns.png`, ZIP-ul începe la offsetul `782`. Conține `secret.txt`, cu mesajul `FLAG{ascuns_prin_carving}`.
- **Mesajul LSB din stego.png:** `FLAG{ascuns_in_pixeli}`.

## Provocarea opțională

Pentru `challenge.bin` am desfăcut stratul Base64 și am încercat cheile XOR. Cu cheia `128` am obținut `FLAG{lant_complet_despicat}`. Hash-ul MD5 al mesajului este `8c4eb02d9dcef7d0ff91d8e4c7fea91b`, identic cu cel din indiciu.
