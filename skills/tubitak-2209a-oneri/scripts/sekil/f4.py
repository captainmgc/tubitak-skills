from lib import *

W, H = 1200, 590
G = 485  # ground line
o = []
o.append(f'<rect x="0" y="0" width="{W}" height="{G}" fill="#e3f2fd"/>')
o.append(f'<rect x="0" y="{G}" width="{W}" height="{H - G}" fill="#9c6644"/>')
o.append(f'<rect x="0" y="{G}" width="{W}" height="14" fill="#7f5539"/>')
for sx, sy in [(60, 560), (330, 545), (520, 570), (700, 550), (980, 565), (1130, 545), (850, 575)]:
    o.append(f'<ellipse cx="{sx}" cy="{sy}" rx="16" ry="6" fill="#7f5539" opacity="0.7"/>')
o.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="none" stroke="#333" stroke-width="4"/>')

# ---- collapsed building
o.append('<polygon points="40,485 40,255 98,262 104,330 88,485" fill="#adb5bd" stroke="#6c757d" stroke-width="3"/>')
for wy in (285, 335, 385):
    o.append(rect(52, wy, 26, 24, "#6c757d", rx=2))
slabs = ["70,420 330,365 338,385 78,442", "95,365 300,320 306,338 100,384",
         "120,470 340,445 345,462 118,485", "300,320 345,400 333,404 290,330"]
o.append('<polygon points="88,485 345,485 345,400 300,345 140,380 96,405" fill="#ced4da"/>')
for s in slabs:
    o.append(f'<polygon points="{s}" fill="#8d99ae" stroke="#5c677d" stroke-width="3" stroke-linejoin="round"/>')
for bx, by, r in [(130, 455, 9), (290, 470, 11), (320, 430, 8), (110, 395, 7), (250, 350, 9)]:
    o.append(f'<circle cx="{bx}" cy="{by}" r="{r}" fill="#9aa5b1"/>')
# cavity with trapped person
o.append('<path d="M150,447 Q200,420 270,437 L272,462 L150,467 Z" fill="#343a40"/>')
o.append(lying_person(205, 452, 0.62, "#457b9d"))
o.append(phone(246, 438, 16, 26, body="#111", screen="#7dd3fc"))
o.append(waves(254, 440, 18, 3, "#38bdf8", -55, spread=35, gap=13, sw=4))

# tower + callout
o.append(tower(70, 250, 0.55))
o.append(rect(165, 120, 160, 46, "#e63946", rx=10))
o.append(text(245, 143, "Şebeke yok", size=21, fill="#fff"))
o.append('<path d="M165,150 L118,178" stroke="#e63946" stroke-width="4"/>')

# label under rubble
o.append(f'<path d="M254,466 L254,520" stroke="#fff" stroke-width="3" stroke-dasharray="5 4"/>')
o.append(rect(150, 520, 210, 42, "#fff", rx=8, stroke="#e63946", sw=3))
o.append(text(255, 541, "Afetzede telefonu", size=20, fill="#c1121f"))

# ---- relays
rel = [430, 590, 750]
shirts = ["#2a9d8f", "#8e44ad", "#e76f51"]
for x, c in zip(rel, shirts):
    o.append(person(x, G, 1.0, shirt=c, arm_up=True))
    o.append(phone(x + 27, G - 100, 18, 30, body="#111", screen="#7dd3fc"))
    o.append(waves(x + 46, G - 85, 14, 2, "#38bdf8", 0, spread=40, gap=11, sw=3.5))
o.append(text(590, 250, "Röle telefonlar\n(taşı-sakla-ilet)", size=22, lh=27))
o.append('<path d="M436,318 L596,318" stroke="#333" stroke-width="2.5"/>'
         '<path d="M436,308 L436,328 M596,308 L596,328" stroke="#333" stroke-width="2.5"/>')
o.append(text(516, 302, "BLE ≈ 30–50 m", size=18, fill="#333"))

# ---- data-flow arrows (green)
o.append(block_arrow(285, 405, 395, 380, w=18, head=22, fill="#7bd36b", stroke="#2b7a2b"))
o.append(block_arrow(480, 380, 560, 380, w=18, head=22, fill="#7bd36b", stroke="#2b7a2b"))
o.append(block_arrow(640, 380, 720, 380, w=18, head=22, fill="#7bd36b", stroke="#2b7a2b"))
o.append(block_arrow(800, 380, 852, 380, w=18, head=22, fill="#7bd36b", stroke="#2b7a2b"))

# ---- rescue worker
wx = 900
o.append(person(wx, G, 1.05, vest="#f77f00", helmet="#ffd60a", arm_up=True))
o.append(rect(wx + 22, G - 112, 34, 26, "#22223b", rx=4) + rect(wx + 26, G - 108, 26, 18, "#fff", rx=2))
o.append(tablet(800, 105, 200, 132, rows=3, with_map=True))
o.append(f'<path d="M{wx + 40},{G - 114} L900,240" stroke="#555" stroke-width="2.5" stroke-dasharray="5 5"/>')
o.append(text(900, 82, "Kurtarma ekibi cihazı", size=20, fill="#1d3557"))

# ---- future integration (dashed)
bx, by, bw, bh = 1022, 95, 162, 250
o.append(rect(bx, by, bw, bh, "#fff", rx=12, stroke="#6c757d", sw=3, extra='stroke-dasharray="9 7"'))
o.append('<path d="M1065,160 a22,22 0 0 1 40,-12 a26,26 0 0 1 46,16 a18,18 0 0 1 -4,34 h-80 a20,20 0 0 1 -2,-38 z" fill="#90caf9"/>')
o.append(text(bx + bw / 2, by + 168, "Şebeke\ndöndüğünde:\nafet yönetim\nsistemlerine\naktarım", size=17, weight="bold", fill="#444", lh=20))
o.append(text(bx + bw / 2, by + 228, "(gelecek çalışma)", size=15, weight="normal", fill="#666", italic=True))
o.append(f'<path d="M{wx + 60},{G - 100} C980,380 1000,370 1060,{by + bh + 4}" fill="none" stroke="#6c757d" stroke-width="3.5" stroke-dasharray="8 6"/>')
o.append(f'<polygon points="1060,{by + bh} 1050,{by + bh + 20} 1072,{by + bh + 16}" fill="#6c757d"/>')
save_render("sekil4_sistem", "".join(o), W, H)
