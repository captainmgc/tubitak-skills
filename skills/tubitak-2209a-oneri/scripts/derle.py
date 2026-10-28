"""uretim/oneri_kaynak.md -> <AD>_oneri_metni.md, kaynaklar.md, <AD>_TYBS_metni_tam.md, DOI_tiklama_listesi.md
[@anahtar] atıfları ilk geçiş sırasına göre [1], [2] ... olarak numaralanır.

Çalıştırma:  python <beceri>/scripts/derle.py [proje_kökü]   (varsayılan: çalışılan dizin)
Proje kökünde gereken dosyalar:
  proje.json              {"ad": "PROJE_2026", "anahtarlar": {"karaman": "Karaman, B.", ...}}
  uretim/oneri_kaynak.md  metin; atıflar [@anahtar]
  uretim/kaynak_havuzu.md başlık satırı + boş satırla ayrılmış doğrulanmış kaynaklar
'anahtarlar': anahtar -> kaynak_havuzu.md içindeki girdinin başı (tek girdiyle eşleşmeli)."""
import datetime, json, os, re, sys

os.chdir(sys.argv[1] if len(sys.argv) > 1 else os.getcwd())
AYAR = json.load(open('proje.json', encoding='utf-8'))
AD, ANAHTAR = AYAR['ad'], AYAR['anahtarlar']

havuz = [e.strip() for e in open('uretim/kaynak_havuzu.md', encoding='utf-8').read().split('\n\n')[1:] if e.strip()]
def girdi(k):
    m = [e for e in havuz if e.startswith(ANAHTAR[k])]
    assert len(m) == 1, (k, len(m)); return m[0]

src = open('uretim/oneri_kaynak.md', encoding='utf-8').read()
sira = []
def no(m):
    k = m.group(1)
    if k not in sira: sira.append(k)
    return f'[{sira.index(k)+1}]'
metin = re.sub(r'\[@([a-z0-9_]+)\]', no, src)
assert '[@' not in metin

kay = ['## KAYNAKLAR', '']
for i, k in enumerate(sira, 1):
    e = re.sub(r'^(.*?\(\d{4})[a-z]\)', r'\1)', girdi(k))  # numaralı biçimde 2023a -> 2023
    kay += [f'[{i}] {e}', '']
kay_md = '\n'.join(kay).rstrip() + '\n'

open(f'{AD}_oneri_metni.md', 'w', encoding='utf-8').write(metin)
open('kaynaklar.md', 'w', encoding='utf-8').write(kay_md)
open(f'{AD}_TYBS_metni_tam.md', 'w', encoding='utf-8').write(metin.replace('{{KAYNAKLAR}}', kay_md))
doili = [(i, e) for i, e in enumerate([l[l.index(' ')+1:] for l in kay[2::2]], 1) if 'DOI: ' in e]
tik = [f'# DOI tıklama listesi ({len(doili)} kaynak)', '',
       'Her bağlantıyı tarayıcıda açın. Açılan sayfadaki makale başlığı ve yazarlar buradakiyle aynıysa kaynak doğrudur. '
       f'Liste {datetime.date.today():%d.%m.%Y} tarihinde üretildi; TÜBİTAK ÜYZ Rehberi gereği başvuru sahibinin kendi son kontrolü içindir.', '',
       '| No | Kaynak | Bağlantı | Kontrol |', '|---|---|---|---|']
for i, e in doili:
    tik.append(f'| [{i}] | {e[:110]}… | https://doi.org/{e.split("DOI: ")[1].strip()} | ☐ |')
tik += ['', f'DOI olmayan {len(sira) - len(doili)} resmî belge/web kaynağının URL\'leri kaynakçada yazılıdır.']
open('DOI_tiklama_listesi.md', 'w', encoding='utf-8').write('\n'.join(tik) + '\n')
atifsiz = sorted(set(ANAHTAR) - set(sira))
print(len(sira), 'kaynak,', len(doili), "DOI'li" + (' | atıfsız anahtar: ' + ', '.join(atifsiz) if atifsiz else ''))
