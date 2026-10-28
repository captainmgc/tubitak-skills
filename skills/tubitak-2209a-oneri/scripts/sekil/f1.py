from lib import *

W, H = 1200, 570
o = []
CX0, CX1, CY = 480, 720, 285
branches = [
    # side, cy, title, color, pale, text-on-primary, subs
    ("L", 100, "Şebeke\nKesintisi", "#e63946", "#fde2e4", "#fff",
     ["8.900 baz istasyonundan\n2.451'i devre dışı", "Hasarlı kapasitenin\n%40'ı 48 saatte geri geldi"]),
    ("L", 285, "Sağkalım\nPenceresi", "#2541d6", "#dde3fb", "#fff",
     ["Canlı kurtarmaların\n%89'u ilk 24 saatte", "Crush hastalarının\n%97'si ilk 48 saatte"]),
    ("L", 470, "Adres ve Konum\nBelirsizliği", "#f2b705", "#fdf1c7", "#222",
     ["Eşleşmeyen\nihbar adresleri", "Sosyal medyaya\nbağımlı ihbarlar"]),
    ("R", 100, "Mevcut\nSistemler", "#12c2b0", "#d5f5f1", "#123",
     ["Şebekeye bağımlı", "Tek yönlü uyarı"]),
    ("R", 285, "Kırılgan\nGruplar", "#8e44ad", "#eadcf2", "#fff",
     ["Yaşlı, engelli,\nkronik hasta"]),
    ("R", 470, "Fırsat: Cebimizdeki\nTelefon", "#2b9348", "#d8f3dc", "#fff",
     ["Mobil işletim sisteminde\n%77 Android", "Bluetooth Düşük\nEnerji (BLE)"]),
]
PW, PH = 200, 66
SW, SH = 232, 56
for side, cy, title, col, pale, tc, subs in branches:
    if side == "L":
        px = 250; sx = 8
        start = (CX0 + 50, CY - 30) if cy < CY else ((CX0, CY) if cy == CY else (CX0 + 50, CY + 30))
        end = (px + PW, cy)
        sub_anchor_x, p_out = sx + SW, px
    else:
        px = 750; sx = 1200 - 8 - SW
        start = (CX1 - 50, CY - 30) if cy < CY else ((CX1, CY) if cy == CY else (CX1 - 50, CY + 30))
        end = (px, cy)
        sub_anchor_x, p_out = sx, px + PW
    # connector centre -> primary
    sx0, sy0 = start
    ex, ey = end
    o.append(f'<path d="M{sx0},{sy0} C{sx0},{ey} {(sx0 + ex) / 2},{ey} {ex},{ey}" fill="none" stroke="{col}" stroke-width="5" stroke-linecap="round"/>')
    o.append(rect(px, cy - PH / 2, PW, PH, col, rx=10))
    o.append(text(px + PW / 2, cy, title, size=20, fill=tc))
    n = len(subs)
    gap = 10
    tot = n * SH + (n - 1) * gap
    for i, s in enumerate(subs):
        sy = cy - tot / 2 + i * (SH + gap)
        scy = sy + SH / 2
        o.append(f'<path d="M{p_out},{cy} C{(p_out + sub_anchor_x) / 2},{cy} {(p_out + sub_anchor_x) / 2},{scy} {sub_anchor_x},{scy}" '
                 f'fill="none" stroke="{col}" stroke-width="3"/>')
        o.append(rect(sx, sy, SW, SH, pale, rx=10))
        o.append(text(sx + SW / 2, scy, s, size=17, weight="normal", fill="#222", lh=20))
# centre on top
o.append(rect(CX0, CY - 48, CX1 - CX0, 96, "#111", rx=14))
o.append(text((CX0 + CX1) / 2, CY, "Deprem Sonrası\nİlk Saatler", size=27, fill="#fff", lh=33))
save_render("sekil1_zihin_haritasi", "".join(o), W, H)
