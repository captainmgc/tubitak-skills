from lib import *
import random

W, H = 1200, 650
TW, TH = 300, 170
COLS = [60, 450, 840]
o = []


def frame(x, y):
    return rect(x, y, TW, TH, "#f8f9fa", rx=6, stroke="#adb5bd", sw=2)


def t1(x, y):
    s = [frame(x, y)]
    widths = [1, 4, 4, 4, 1, 3, 1, 1, 1, 1, 1, 4]
    pal = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51", "#8ecae6", "#219ebc", "#ffb703", "#fb8500", "#8338ec", "#3a86ff", "#adb5bd"]
    tot = sum(widths)
    cx = x + 15
    for w, c in zip(widths, pal):
        ww = 270 * w / tot
        s.append(f'<rect x="{cx:.1f}" y="{y + 22}" width="{ww - 2:.1f}" height="34" fill="{c}" rx="2"/>')
        cx += ww
    s.append(text(x + TW / 2, y + 78, "26 bayt", size=20, fill="#222"))
    icons = [heart(0, 0, 0.9), clock(0, 0, 10), battery(-12, -7, 22, 14, 0.4), star(0, 0, 11)]
    lens = [0.9, 0.6, 0.35, 0.75]
    for i, (ic, ln) in enumerate(zip(icons, lens)):
        yy = y + 104 + i * 17
        xx = x + 40 + (i % 2) * 135
        yy = y + 108 + (i // 2) * 34
        s.append(f'<g transform="translate({xx},{yy})">{ic}</g>')
        s.append(rect(xx + 20, yy - 6, 90 * ln, 12, "#457b9d", rx=3))
    return "".join(s)


def t2(x, y):
    px, py = x + 110, y + 10
    inner = (rect(px + 9, py + 22, 62, 24, "#e63946", rx=4) + text(px + 40, py + 34, "SOS", size=16, fill="#fff") +
             ble_logo(px + 40, py + 90, 36, "#1d4ed8"))
    return frame(x, y) + phone(px, py, 80, 150, inner=inner) + waves(px + 82, py + 80, 16, 3, "#1d4ed8", 0, gap=13) + \
        waves(px - 2, py + 80, 16, 3, "#1d4ed8", 180, gap=13)


def t3(x, y):
    return frame(x, y) + tablet(x + 25, y + 15, 250, 140, rows=3, with_map=True)


def t4(x, y):
    random.seed(4)
    s = [frame(x, y), rect(x + 8, y + 8, TW - 16, TH - 16, "#e9f5db", rx=4),
         f'<path d="M{x + 8},{y + 110} L{x + TW - 8},{y + 70}" stroke="#fff" stroke-width="10"/>',
         f'<path d="M{x + 120},{y + 8} L{x + 170},{y + TH - 8}" stroke="#fff" stroke-width="10"/>']
    pts = [(x + random.randint(25, TW - 25), y + random.randint(22, TH - 22)) for _ in range(16)]
    for i, a in enumerate(pts):
        for b in pts[i + 1:]:
            if math.dist(a, b) < 70:
                s.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#6c757d" stroke-width="2"/>')
    for i, (px, py) in enumerate(pts):
        c = "#e63946" if i in (0, 5) else ("#1d4ed8" if i % 3 else "#2a9d8f")
        s.append(f'<circle cx="{px}" cy="{py}" r="7" fill="{c}" stroke="#fff" stroke-width="2"/>')
    return "".join(s)


def t5(x, y):
    s = [frame(x, y)]
    for bx, bw, bh in [(x + 20, 70, 70), (x + 105, 55, 100), (x + 175, 80, 60)]:
        s.append(rect(bx, y + TH - 18 - bh, bw, bh, "#ced4da", rx=2, stroke="#868e96", sw=2))
        for k in range(2):
            s.append(rect(bx + 10, y + TH - 10 - bh + 12 + k * 26, bw - 20, 10, "#a8dadc", rx=1))
    s.append(f'<line x1="{x + 8}" y1="{y + TH - 18}" x2="{x + TW - 8}" y2="{y + TH - 18}" stroke="#6d4c41" stroke-width="4"/>')
    for px, py in [(x + 60, y + 60), (x + 150, y + 50), (x + 230, y + 95)]:
        s.append(f'<circle cx="{px}" cy="{py}" r="34" fill="#3a86ff" opacity="0.12" stroke="#3a86ff" stroke-dasharray="5 4" stroke-width="2"/>')
        s.append(phone(px - 7, py - 12, 14, 24, body="#111", screen="#7dd3fc"))
    s.append(battery(x + 222, y + 18, 52, 26, 0.8, "#2b9348"))
    return "".join(s)


def t6(x, y):
    s = [frame(x, y)]
    bx, by = x + 25, y + TH - 25
    s.append(f'<path d="M{bx},{y + 20} L{bx},{by} L{bx + 160},{by}" fill="none" stroke="#333" stroke-width="2.5"/>')
    for i, (h, c) in enumerate([(60, "#8ecae6"), (95, "#219ebc"), (80, "#ffb703"), (120, "#fb8500")]):
        s.append(rect(bx + 14 + i * 36, by - h, 24, h, c, rx=2))
    for k, dx in enumerate((210, 262)):
        s.append(person(x + dx, y + TH - 22, 0.95, shirt=["#2a9d8f", "#8e44ad"][k]))
    s.append(f'<circle cx="{x + 236}" cy="{y + 30}" r="17" fill="#2b9348"/>'
             f'<path d="M{x + 227},{y + 30} l7,7 l12,-14" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')
    return "".join(s)


blocks = [
    (0, 0, "1. Paket ve skor tasarımı", t1, "İA1 · Ay 1–2"),
    (1, 0, "2. Afetzede uygulaması", t2, "İA2 · Ay 2–5"),
    (2, 0, "3. Ekip uygulaması", t3, "İA3 · Ay 4–6"),
    (2, 1, "4. Benzetim (ONE)", t4, "İA4 · Ay 5–7"),
    (1, 1, "5. Laboratuvar ve saha ölçümleri", t5, "İA5 · Ay 7–10"),
    (0, 1, "6. Uzman doğrulaması ve sonuçlar", t6, "İA6 · Ay 10–12"),
]
for col, row, title, fn, lab in blocks:
    x = COLS[col]
    ty = 45 if row == 0 else 395
    y = ty + 25
    o.append(text(x + TW / 2, ty, title, size=20, fill="#111"))
    o.append(fn(x, y))
    o.append(rect(x + TW / 2 - 75, y + TH + 10, 150, 30, "#1d3557", rx=15))
    o.append(text(x + TW / 2, y + TH + 25, lab, size=16, fill="#fff"))

o.append(block_arrow(366, 155, 444, 155))
o.append(block_arrow(756, 155, 834, 155))
o.append(block_arrow(990, 292, 990, 372))
o.append(block_arrow(834, 505, 756, 505))
o.append(block_arrow(444, 505, 366, 505))
save_render("sekil5_yontem_akisi", "".join(o), W, H)
