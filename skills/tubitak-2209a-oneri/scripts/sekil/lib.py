import math, os, subprocess

# Çıktı klasörü: SEKIL_CIKTI ortam değişkeni ya da çalışılan dizindeki sekiller/
OUT = os.environ.get("SEKIL_CIKTI", os.path.join(os.getcwd(), "sekiller"))
os.makedirs(OUT, exist_ok=True)
CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=18, weight="bold", fill="#222", anchor="middle", lh=None, italic=False):
    """Multi-line text vertically centred on y."""
    lines = s.split("\n")
    lh = lh or size * 1.2
    y0 = y - (len(lines) - 1) * lh / 2 + size * 0.35
    st = ' font-style="italic"' if italic else ""
    out = [f'<text x="{x}" y="{y0:.1f}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{st}>']
    for i, ln in enumerate(lines):
        dy = 0 if i == 0 else lh
        out.append(f'<tspan x="{x}" dy="{dy:.1f}">{esc(ln)}</tspan>')
    out.append("</text>")
    return "".join(out)


def rect(x, y, w, h, fill, rx=8, stroke="none", sw=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


def page(svg_body, w, h):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;background:#fff}}'
            f'svg{{display:block}}</style></head><body>'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'font-family="Arial, Helvetica, sans-serif">{svg_body}</svg></body></html>')


def save_render(name, body, w, h):
    html = os.path.join(OUT, name + ".html")
    png = os.path.join(OUT, name + ".png")
    with open(html, "w", encoding="utf-8") as f:
        f.write(page(body, w, h))
    url = "file:///" + html.replace("\\", "/")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=2", f"--window-size={w},{h}",
                    f"--screenshot={png}", url], check=True, capture_output=True)
    print(png)


# ---------------------------------------------------------------- icons

def waves(cx, cy, r0, n, color, ang, spread=38, gap=13, sw=4):
    out = []
    for i in range(n):
        r = r0 + i * gap
        a1, a2 = math.radians(ang - spread), math.radians(ang + spread)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        out.append(f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 0 1 {x2:.1f},{y2:.1f}" fill="none" '
                   f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round" opacity="{1 - i * 0.18:.2f}"/>')
    return "".join(out)


def phone(x, y, w, h, body="#2b2d42", screen="#eaf4ff", inner=""):
    """x,y top-left."""
    r = w * 0.16
    return (rect(x, y, w, h, body, rx=r) +
            rect(x + w * 0.08, y + h * 0.1, w * 0.84, h * 0.78, screen, rx=r * 0.3) +
            f'<circle cx="{x + w / 2}" cy="{y + h * 0.94}" r="{w * 0.05}" fill="#8d99ae"/>' + inner)


def ble_logo(cx, cy, s, color="#fff"):
    # stylised bluetooth rune
    p = (f"M{cx - 0.35 * s},{cy - 0.3 * s} L{cx + 0.35 * s},{cy + 0.3 * s} L{cx},{cy + 0.6 * s} "
         f"L{cx},{cy - 0.6 * s} L{cx + 0.35 * s},{cy - 0.3 * s} L{cx - 0.35 * s},{cy + 0.3 * s}")
    return f'<path d="{p}" fill="none" stroke="{color}" stroke-width="{0.12 * s}" stroke-linejoin="round" stroke-linecap="round"/>'


def tower(x, y, s=1.0, crossed=True):
    """x,y = base centre."""
    h = 120 * s
    w = 34 * s
    top = y - h
    o = [f'<g stroke="#4a4e69" stroke-width="{4 * s}" stroke-linecap="round" fill="none">',
         f'<path d="M{x - w},{y} L{x},{top} L{x + w},{y}"/>']
    for k in range(1, 4):
        yy = y - h * k / 4
        dx = w * (1 - k / 4)
        o.append(f'<path d="M{x - dx},{yy} L{x + dx},{yy}"/>')
        o.append(f'<path d="M{x - dx},{yy} L{x + w * (1 - (k - 1) / 4)},{y - h * (k - 1) / 4}"/>')
    o.append("</g>")
    o.append(f'<rect x="{x - 14 * s}" y="{top - 4 * s}" width="{9 * s}" height="{22 * s}" rx="{2 * s}" fill="#4a4e69"/>')
    o.append(f'<rect x="{x + 5 * s}" y="{top - 4 * s}" width="{9 * s}" height="{22 * s}" rx="{2 * s}" fill="#4a4e69"/>')
    o.append(waves(x, top + 4 * s, 22 * s, 2, "#9aa5b1", -90, spread=45, gap=12 * s, sw=3 * s))
    if crossed:
        cy = y - h * 0.55
        r = 70 * s
        o.append(f'<circle cx="{x}" cy="{cy}" r="{r}" fill="none" stroke="#e63946" stroke-width="{9 * s}"/>')
        o.append(f'<line x1="{x - r * 0.7}" y1="{cy - r * 0.7}" x2="{x + r * 0.7}" y2="{cy + r * 0.7}" '
                 f'stroke="#e63946" stroke-width="{9 * s}" stroke-linecap="round"/>')
    return "".join(o)


def person(x, y, s=1.0, shirt="#457b9d", pants="#1d3557", skin="#f2c39b", helmet=None, vest=None, arm_up=False):
    """x,y = feet centre. height ~ 110*s"""
    o = []
    # legs
    o.append(f'<path d="M{x - 9 * s},{y} L{x - 7 * s},{y - 42 * s} L{x + 7 * s},{y - 42 * s} L{x + 9 * s},{y}" '
             f'fill="none" stroke="{pants}" stroke-width="{11 * s}" stroke-linecap="round" stroke-linejoin="round"/>')
    # body
    o.append(rect(x - 16 * s, y - 82 * s, 32 * s, 44 * s, vest or shirt, rx=10 * s))
    if vest:
        o.append(f'<rect x="{x - 16 * s}" y="{y - 64 * s}" width="{32 * s}" height="{5 * s}" fill="#f1faee"/>')
        o.append(f'<rect x="{x - 16 * s}" y="{y - 52 * s}" width="{32 * s}" height="{5 * s}" fill="#f1faee"/>')
    # arms
    if arm_up:
        o.append(f'<path d="M{x + 13 * s},{y - 76 * s} L{x + 30 * s},{y - 62 * s} L{x + 34 * s},{y - 78 * s}" fill="none" '
                 f'stroke="{vest or shirt}" stroke-width="{9 * s}" stroke-linecap="round" stroke-linejoin="round"/>')
    else:
        o.append(f'<path d="M{x + 14 * s},{y - 76 * s} L{x + 20 * s},{y - 46 * s}" stroke="{vest or shirt}" '
                 f'stroke-width="{9 * s}" stroke-linecap="round"/>')
    o.append(f'<path d="M{x - 14 * s},{y - 76 * s} L{x - 20 * s},{y - 46 * s}" stroke="{vest or shirt}" '
             f'stroke-width="{9 * s}" stroke-linecap="round"/>')
    # head
    o.append(f'<circle cx="{x}" cy="{y - 97 * s}" r="{13 * s}" fill="{skin}"/>')
    if helmet:
        o.append(f'<path d="M{x - 16 * s},{y - 99 * s} A{16 * s},{16 * s} 0 0 1 {x + 16 * s},{y - 99 * s} Z" fill="{helmet}"/>')
        o.append(f'<rect x="{x - 19 * s}" y="{y - 101 * s}" width="{38 * s}" height="{5 * s}" rx="{2 * s}" fill="{helmet}"/>')
    else:
        o.append(f'<path d="M{x - 13 * s},{y - 99 * s} A{13 * s},{13 * s} 0 0 1 {x + 13 * s},{y - 99 * s} '
                 f'Q{x},{y - 104 * s} {x - 13 * s},{y - 99 * s} Z" fill="#3d2c22"/>')
    return "".join(o)


def pin(x, y, s=1.0, color="#e63946"):
    """x,y = tip."""
    return (f'<path d="M{x},{y} C{x - 6 * s},{y - 10 * s} {x - 14 * s},{y - 18 * s} {x - 14 * s},{y - 27 * s} '
            f'A{14 * s},{14 * s} 0 1 1 {x + 14 * s},{y - 27 * s} C{x + 14 * s},{y - 18 * s} {x + 6 * s},{y - 10 * s} {x},{y} Z" fill="{color}"/>'
            f'<circle cx="{x}" cy="{y - 27 * s}" r="{5.5 * s}" fill="#fff"/>')


def clock(cx, cy, r, color="#2a9d8f"):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{color}" stroke-width="{r * 0.22}"/>'
            f'<path d="M{cx},{cy - r * 0.55} L{cx},{cy} L{cx + r * 0.45},{cy + r * 0.2}" fill="none" stroke="{color}" '
            f'stroke-width="{r * 0.18}" stroke-linecap="round"/>')


def battery(x, y, w, h, level=0.6, color="#2a9d8f"):
    return (rect(x, y, w, h, "#fff", rx=h * 0.18, stroke="#333", sw=h * 0.1) +
            rect(x + w, y + h * 0.3, w * 0.08, h * 0.4, "#333", rx=1) +
            rect(x + h * 0.14, y + h * 0.14, (w - h * 0.28) * level, h * 0.72, color, rx=h * 0.08))


def heart(cx, cy, s, color="#e63946"):
    return (f'<path d="M{cx},{cy + 9 * s} C{cx - 14 * s},{cy} {cx - 12 * s},{cy - 12 * s} {cx - 5 * s},{cy - 11 * s} '
            f'C{cx - 2 * s},{cy - 11 * s} {cx},{cy - 8 * s} {cx},{cy - 6 * s} C{cx},{cy - 8 * s} {cx + 2 * s},{cy - 11 * s} '
            f'{cx + 5 * s},{cy - 11 * s} C{cx + 12 * s},{cy - 12 * s} {cx + 14 * s},{cy} {cx},{cy + 9 * s} Z" fill="{color}"/>')


def star(cx, cy, r, color="#f4a261"):
    pts = []
    for i in range(10):
        a = math.radians(-90 + i * 36)
        rr = r if i % 2 == 0 else r * 0.45
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{color}"/>'


def tablet(x, y, w, h, rows=3, with_map=True):
    """priority list (+ optional mini map)."""
    o = [rect(x, y, w, h, "#22223b", rx=12), rect(x + 10, y + 10, w - 20, h - 20, "#fff", rx=5)]
    cols = ["#e63946", "#f4a261", "#e9c46a", "#90be6d"]
    lw = (w - 20) * (0.55 if with_map else 1)
    rh = (h - 30) / rows
    for i in range(rows):
        ry = y + 15 + i * rh
        cy = ry + rh / 2
        r = min(rh * 0.32, 13)
        o.append(f'<circle cx="{x + 18 + r}" cy="{cy}" r="{r}" fill="{cols[i]}"/>')
        o.append(text(x + 18 + r, cy, str(i + 1), size=r * 1.25, fill="#fff"))
        o.append(rect(x + 26 + 2 * r, cy - rh * 0.16, lw - 34 - 2 * r, rh * 0.13, "#adb5bd", rx=2))
        o.append(rect(x + 26 + 2 * r, cy + rh * 0.06, (lw - 34 - 2 * r) * 0.6, rh * 0.1, "#dee2e6", rx=2))
    if with_map:
        mx, my, mw, mh = x + 10 + lw + 4, y + 14, w - 24 - lw - 4 - 4, h - 28
        o.append(rect(mx, my, mw, mh, "#e9f5db", rx=4))
        o.append(f'<path d="M{mx},{my + mh * 0.6} L{mx + mw},{my + mh * 0.35}" stroke="#fff" stroke-width="{mw * 0.08}"/>')
        o.append(f'<path d="M{mx + mw * 0.35},{my} L{mx + mw * 0.55},{my + mh}" stroke="#fff" stroke-width="{mw * 0.08}"/>')
        ps = mw / 120
        o.append(pin(mx + mw * 0.25, my + mh * 0.45, ps, cols[0]))
        o.append(pin(mx + mw * 0.75, my + mh * 0.3, ps, cols[1]))
        o.append(pin(mx + mw * 0.65, my + mh * 0.85, ps, cols[2]))
    return "".join(o)


def house(cx, base, s=1.0, shake=True):
    w, h = 110 * s, 70 * s
    o = [rect(cx - w / 2, base - h, w, h, "#f1faee", rx=3, stroke="#457b9d", sw=4 * s),
         f'<polygon points="{cx - w / 2 - 12 * s},{base - h} {cx},{base - h - 50 * s} {cx + w / 2 + 12 * s},{base - h}" fill="#e63946"/>',
         rect(cx - 36 * s, base - h + 14 * s, 22 * s, 20 * s, "#a8dadc", rx=2),
         rect(cx + 14 * s, base - h + 14 * s, 22 * s, 20 * s, "#a8dadc", rx=2),
         rect(cx - 11 * s, base - 34 * s, 22 * s, 34 * s, "#8d6e63", rx=2)]
    # crack
    o.append(f'<path d="M{cx + 4 * s},{base - h} l-8,{14 * s} l10,{10 * s} l-9,{14 * s}" fill="none" stroke="#333" stroke-width="{2.5 * s}"/>')
    if shake:
        for side in (-1, 1):
            for k in range(3):
                xx = cx + side * (w / 2 + 22 * s + k * 12 * s)
                o.append(f'<path d="M{xx},{base - h + 5 * s} q{side * 6 * s},{12 * s} 0,{24 * s} q{-side * 6 * s},{12 * s} 0,{24 * s}" '
                         f'fill="none" stroke="#e76f51" stroke-width="{3.5 * s}" stroke-linecap="round" opacity="{1 - k * 0.3:.2f}"/>')
    o.append(f'<line x1="{cx - w / 2 - 50 * s}" y1="{base}" x2="{cx + w / 2 + 50 * s}" y2="{base}" stroke="#6d4c41" stroke-width="{5 * s}" stroke-linecap="round"/>')
    return "".join(o)


def lying_person(cx, cy, s=1.0, shirt="#457b9d"):
    return (f'<circle cx="{cx - 40 * s}" cy="{cy - 4 * s}" r="{12 * s}" fill="#f2c39b"/>'
            + rect(cx - 28 * s, cy - 14 * s, 44 * s, 24 * s, shirt, rx=9 * s)
            + f'<path d="M{cx + 14 * s},{cy - 4 * s} L{cx + 50 * s},{cy - 6 * s} M{cx + 14 * s},{cy + 4 * s} L{cx + 50 * s},{cy + 6 * s}" '
              f'stroke="#1d3557" stroke-width="{10 * s}" stroke-linecap="round"/>')


def handarrow(d, color="#111", sw=9, head=None):
    """hand-drawn-ish arrow along path d; head = (x,y,angle_deg)"""
    o = [f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>']
    if head:
        x, y, a = head
        L = sw * 3.6
        for da in (150, -150):
            ang = math.radians(a + da)
            o.append(f'<path d="M{x},{y} L{x + L * math.cos(ang):.1f},{y + L * math.sin(ang):.1f}" stroke="{color}" '
                     f'stroke-width="{sw}" stroke-linecap="round"/>')
    return "".join(o)


def block_arrow(x1, y1, x2, y2, w=34, head=30, fill="#ffd93d", stroke="#5c5c5c"):
    """thick filled arrow from (x1,y1) to (x2,y2)."""
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    bx, by = x2 - ux * head, y2 - uy * head
    hw, hh = w / 2, w / 2 + 14
    pts = [(x1 + nx * hw, y1 + ny * hw), (bx + nx * hw, by + ny * hw), (bx + nx * hh, by + ny * hh), (x2, y2),
           (bx - nx * hh, by - ny * hh), (bx - nx * hw, by - ny * hw), (x1 - nx * hw, y1 - ny * hw)]
    p = " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)
    return f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="3" stroke-linejoin="round"/>'
