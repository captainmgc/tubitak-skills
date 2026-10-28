from lib import *

W, H = 1200, 640
X0, X1, Y0, Y1 = 110, 1150, 470, 110


def X(t): return X0 + (X1 - X0) * t / 168
def Y(v): return Y0 - (Y0 - Y1) * v / 100


o = []
# critical window
o.append(f'<rect x="{X(0)}" y="{Y1}" width="{X(48) - X(0)}" height="{Y0 - Y1}" fill="#fde2e4"/>')
o.append(f'<path d="M{X(0)},{Y1 - 14} L{X(0)},{Y1 - 24} L{X(48)},{Y1 - 24} L{X(48)},{Y1 - 14}" fill="none" stroke="#c1121f" stroke-width="3"/>')
o.append(text((X(0) + X(48)) / 2, Y1 - 52, "Kritik pencere: şebeke yok, sağkalım en yüksek", size=20, fill="#c1121f"))
# grid
for v in range(0, 101, 20):
    o.append(f'<line x1="{X0}" y1="{Y(v)}" x2="{X1}" y2="{Y(v)}" stroke="#ddd" stroke-width="1.5"/>')
    o.append(text(X0 - 14, Y(v), f"%{v}", size=18, weight="normal", fill="#444", anchor="end"))
for t in range(0, 169, 24):
    o.append(f'<line x1="{X(t)}" y1="{Y0}" x2="{X(t)}" y2="{Y0 + 8}" stroke="#333" stroke-width="2"/>')
    o.append(text(X(t), Y0 + 26, str(t), size=18, weight="normal", fill="#333"))
o.append(f'<line x1="{X0}" y1="{Y0}" x2="{X1}" y2="{Y0}" stroke="#333" stroke-width="2.5"/>')
o.append(f'<line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1}" stroke="#333" stroke-width="2.5"/>')
o.append(text((X0 + X1) / 2, Y0 + 60, "Depremden sonra geçen süre (saat)", size=20, fill="#222"))
# orange: capacity
cap = [(0, 0), (24, 3), (48, 40), (168, 80)]
o.append('<polyline points="' + " ".join(f"{X(t)},{Y(v)}" for t, v in cap) +
         '" fill="none" stroke="#f77f00" stroke-width="5" stroke-linejoin="round"/>')
for t, v in cap:
    o.append(f'<circle cx="{X(t)}" cy="{Y(v)}" r="8" fill="#f77f00" stroke="#fff" stroke-width="2.5"/>')
o.append(text(X(24) - 50, Y(3) - 26, "≈ %0", size=18, fill="#c75000"))
o.append(text(X(48) + 46, Y(40) + 6, "%40", size=18, fill="#c75000"))
o.append(text(X(168) - 6, Y(80) - 24, "%80", size=18, fill="#c75000"))
# blue: rescues
o.append(f'<path d="M{X(0)},{Y(0)} L{X(24)},{Y(89)}" stroke="#1d4ed8" stroke-width="3" stroke-dasharray="8 7" fill="none"/>')
o.append(f'<path d="M{X(24)},{Y(89)} L{X(48)},{Y(97)}" stroke="#1d4ed8" stroke-width="5" fill="none"/>')
for t, v in [(24, 89), (48, 97)]:
    o.append(f'<circle cx="{X(t)}" cy="{Y(v)}" r="8" fill="#1d4ed8" stroke="#fff" stroke-width="2.5"/>')
o.append(text(X(24) - 34, Y(89) - 6, "%89", size=18, fill="#1d4ed8"))
o.append(text(X(48) + 34, Y(97) + 8, "%97", size=18, fill="#1d4ed8"))
# legend
ly = 575
o.append(f'<line x1="150" y1="{ly}" x2="200" y2="{ly}" stroke="#f77f00" stroke-width="5"/>'
         f'<circle cx="175" cy="{ly}" r="7" fill="#f77f00"/>')
o.append(text(212, ly, "Geri gelen hasarlı mobil kapasite", size=18, weight="normal", anchor="start"))
o.append(f'<line x1="640" y1="{ly}" x2="690" y2="{ly}" stroke="#1d4ed8" stroke-width="5"/>'
         f'<circle cx="665" cy="{ly}" r="7" fill="#1d4ed8"/>')
o.append(text(702, ly, "Enkazdan canlı kurtarmaların birikimli oranı", size=18, weight="normal", anchor="start"))
o.append(text(W / 2, 618, "Kaynak: [1], [2], [3]. Şematik gösterim.",
              size=16, weight="normal", fill="#777"))
save_render("sekil2_kesinti_sagkalim", "".join(o), W, H)
