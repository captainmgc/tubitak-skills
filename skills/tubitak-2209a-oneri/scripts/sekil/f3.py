from lib import *

W, H = 1200, 840
o = []


def badge(x, y, n):
    return f'<circle cx="{x}" cy="{y}" r="22" fill="#111"/>' + text(x, y, str(n), size=24, fill="#fff")


# ---- step 1 (top-left): shaking house + crossed tower + still phone
cx, cy = 240, 200
o.append(house(cx - 135, cy + 70, 0.75))
o.append(text(cx - 135, cy + 102, "Sarsıntı", size=18, weight="normal"))
o.append(tower(cx + 10, cy + 70, 0.75))
o.append(text(cx + 10, cy + 102, "Şebeke yok", size=18, weight="normal"))
# phone with flat motion line
px, py = cx + 105, cy - 40
o.append(phone(px, py, 66, 110, inner=
               f'<path d="M{px + 10},{py + 52} L{px + 22},{py + 52} L{px + 27},{py + 44} L{px + 32},{py + 52} L{px + 56},{py + 52}" '
               f'fill="none" stroke="#e63946" stroke-width="3.5" stroke-linejoin="round"/>'
               f'<rect x="{px + 22}" y="{py + 66}" width="7" height="18" fill="#457b9d"/>'
               f'<rect x="{px + 36}" y="{py + 66}" width="7" height="18" fill="#457b9d"/>'))
o.append(text(px + 33, cy + 102, "Hareketsizlik", size=18, weight="normal"))
o.append(badge(40, 70, 1))
o.append(text(cx, cy + 150, "Deprem, şebeke kaybı ve\nhareketsizlik algılanır", size=22, lh=27))

# ---- step 2 (top-right): phone + packet card
cx, cy = 930, 200
px, py = cx - 255, cy - 75
o.append(phone(px, py, 84, 145, inner=ble_logo(px + 42, py + 62, 40, "#1d4ed8")))
o.append(handarrow(f"M{px + 100},{cy - 5} q30,-6 58,0", "#555", 6, (px + 160, cy - 5, 0)))
kx, ky, kw, kh = cx - 92, cy - 85, 340, 160
o.append(rect(kx, ky, kw, kh, "#fff8e1", rx=14, stroke="#f4a261", sw=4))
o.append(text(kx + kw / 2, ky + 24, "Yaşam ve konum paketi", size=19, fill="#9c4a00"))
icons = [pin(0, 0, 1.1, "#e63946"), clock(0, -26, 20), battery(-24, -38, 42, 24, 0.55),
         heart(0, -24, 1.6), star(0, -26, 22)]
labels = ["Konum", "Zaman", "Pil", "Durum", "Öncelik"]
for i, (ic, lb) in enumerate(zip(icons, labels)):
    ix = kx + 38 + i * 66
    iy = ky + 108
    o.append(f'<g transform="translate({ix},{iy})">{ic}</g>')
    o.append(text(ix, ky + 136, lb, size=16, weight="normal", fill="#333"))
o.append(badge(700, 70, 2))
o.append(text(cx, cy + 150, "Telefon küçük bir yaşam ve\nkonum paketi üretir", size=22, lh=27))

# ---- step 3 (bottom-right): phone chain
cx, cy = 930, 600
xs = [740, 860, 980, 1100]
for i, x in enumerate(xs):
    o.append(phone(x - 30, cy - 70, 60, 104, screen="#eaf4ff", inner=ble_logo(x, cy - 22, 28, "#1d4ed8")))
    if i < 3:
        o.append(waves(x + 30, cy - 18, 14, 3, "#1d4ed8", 0, spread=40, gap=11, sw=4))
        # small envelope moving
        ex = x + 60
        o.append(rect(ex - 13, cy + 46, 26, 18, "#f4a261", rx=3) +
                 f'<path d="M{ex - 13},{cy + 47} L{ex},{cy + 57} L{ex + 13},{cy + 47}" fill="none" stroke="#fff" stroke-width="2.5"/>')
o.append(f'<path d="M{xs[0]},{cy + 82} L{xs[-1]},{cy + 82}" stroke="#1d4ed8" stroke-width="3" stroke-dasharray="7 6"/>')
o.append(text(cx, cy + 102, "her telefon paketi saklar ve iletir", size=18, weight="normal", fill="#1d4ed8"))
o.append(badge(700, 470, 3))
o.append(text(cx, cy + 150, "Paket telefondan\ntelefona taşınır", size=22, lh=27))

# ---- step 4 (bottom-left): rescue worker + tablet
cx, cy = 240, 600
o.append(person(cx - 140, cy + 85, 1.25, vest="#f77f00", helmet="#ffd60a", arm_up=True))
o.append(tablet(cx - 85, cy - 90, 290, 180, rows=3, with_map=True))
o.append(badge(40, 470, 4))
o.append(text(cx, cy + 150, "Ekip öncelik sıralı listeyi\nve haritayı görür", size=22, lh=27))

# ---- big hand-drawn arrows (clockwise)
o.append(handarrow("M470,190 C540,175 600,205 650,188", "#111", 10, (650, 188, -10)))
o.append(handarrow("M1060,375 C1072,410 1062,440 1072,470", "#111", 10, (1072, 470, 80)))
o.append(handarrow("M680,600 C620,615 560,585 505,602", "#111", 10, (505, 602, 168)))
save_render("sekil3_surec", "".join(o), W, H)
