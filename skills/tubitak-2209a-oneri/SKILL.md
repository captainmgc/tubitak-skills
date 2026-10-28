---
name: tubitak-2209a-oneri
description: TÜBİTAK 2209-A (Üniversite Öğrencileri Araştırma Projeleri) araştırma önerisi yazma, sadeleştirme, kaynak doğrulama, şekil çizme ve TÜBİTAK form kalıbında docx/pdf üretme becerisi. Kullanıcı 2209-A, 2209-B, TÜBİTAK öneri formu, TYBS metni, araştırma önerisi, kaynak kontrolü/kaynak doğrulama, DOI kontrolü, "örnek raporlara benzet", "yapay zekâ ile yazılmış gibi duruyor, sadeleştir" veya öneri şekilleri çizme dediğinde kullan. Use for TÜBİTAK 2209-A proposal writing, reference verification via MCP, flat-design figures and docx/pdf generation.
---

# TÜBİTAK 2209-A Araştırma Önerisi Hazırlama

Bu beceri, bir 2209-A başvurusu (YAŞA, 2026) hazırlanırken izlenen yöntemi tarif eder. Amaç, **kabul almış örnek önerilere benzeyen**, kısa, maddeli, kaynakları tek tek doğrulanmış ve TÜBİTAK form kalıbında üretilmiş bir öneri çıkarmaktır.

Bölüm iskeleti ve kalıp cümleler için `sablon.md` dosyasını oku. Betikler bu becerinin `scripts/` klasöründedir (aşağıda `<beceri>` = bu SKILL.md'nin bulunduğu klasör). Kabul almış örnek öneriler beceriyle gelmez; kullanıcıdan proje içinde `ornek_raporlar/` klasörüne koymasını iste.

**Proje klasör yapısı** (çalışılan projenin kökü):
```
proje.json               {"ad": "PROJE_2026", "baslik": "...", "yazar": "...", "ek2": "...", "anahtarlar": {"anahtar": "Havuz girdisinin başı", ...}}
uretim/oneri_kaynak.md   metin; atıflar [@anahtar]; kaynakça yerine {{KAYNAKLAR}}
uretim/kaynak_havuzu.md  ilk satır başlık, sonra boş satırla ayrılmış doğrulanmış kaynaklar
uretim/tubitak_logo.jpg  (isteğe bağlı) form üst logosu; kullanıcı kendisi koyar
sekiller/                şekil PNG'leri (metinde ![Şekil n. ...](sekiller/x.png))
dogrulama_kayitlari/     tarihli MCP doğrulama JSON'ları
ornek_raporlar/          kabul almış örnek öneriler (docx/pdf)
```

## 0. Başlamadan önce

1. **Güncel çağrıyı oku** (her yıl değişir): çağrı duyurusu, başvuru içeriği bilgi notu, Üretken Yapay Zekâ (ÜYZ) rehberi. 2026 kuralları:
   - Başvuru TYBS alanlarına metin girilerek yapılır; dosya yüklenmez.
   - Özet 25–450 kelime; 1.1, 1.2 ve Yöntem en az 350 karakter.
   - Puanlama: Bilimsel nitelik %35, Yöntem %25, Proje yönetimi %20, Yaygın etki %20.
   - Süre en fazla 12 ay; bütçe üst sınırı 12.000 TL (konferans, yayın, patent, konaklama, harcırah yazılamaz).
   - Çalışma takviminde başarı ölçütü puanları toplamı **100**; literatür taraması, rapor yazımı, sonuç paylaşımı ve malzeme alımı **iş adımı olamaz**.
   - Her kaynağa metin içinde atıf zorunlu; DOI'si olan her kaynakta DOI zorunlu.
   - ÜYZ beyanı zorunlu; kaynakların doğruluğundan başvuru sahibi tek başına sorumlu.
   - Marka/kurum adı öne çıkarılmaz (ticari ürün adları metinden çıkarılır).
2. **Kabul almış örnek önerileri incele** (`ornek_raporlar/`). docx'leri `pandoc dosya.docx -t gfm --extract-media=<klasör>` ile aç; görselleri Read ile gör. EMF görselleri PowerShell `System.Drawing.Imaging.Metafile` ile PNG'ye çevir.
3. Belirsiz kararları (kaynak sayısı/biçimi, şekil stili, hangi dosyaların güncelleneceği) **başlamadan tek seferde sor**; tahmin etme.

## 1. Yazım kuralları (örnek önerilerden çıkarıldı)

**Uzunluk ve yapı**
- Kaynakça hariç **yaklaşık 3.000–3.500 kelime**. Örnek öneriler ~3.000 kelime; 7.000 kelimelik metin "yapay zekâ ile yazılmış" izlenimi verdi ve yarıya indirildi.
- Başlıklar 2026 TYBS sırasıyla: Özet → 1.1 → 1.2 → 2. Yöntem → 3.1 Çalışma Takvimi → 3.2 Risk → 3.3 Olanaklar → 4. Yaygın Etki → 5. Diğer → 6. Ekler.
- 1.1'in sonunda madde madde: **"Projenin özgün yönleri;"**, **"Projenin araştırma soruları;"**, **"Projenin hipotezleri;"** (H1–H5).
- 1.2'de madde madde: **"Projenin amacı;"** (fiil + -mak, son madde "-maktır.") ve **"Projenin hedefleri;"** (sayısal, ölçülebilir: "en az %70", "saatte en fazla %2", "en az 0,6 korelasyon").
- Literatür, örnekteki gibi sade bir tabloyla özetlenir: **Konu | Yıl | Kaynak** (yeniden eskiye). Ardından "Tablo 1'deki çalışmalar incelendiğinde şu eksikler görülmektedir:" + maddeler.
- Yöntem: kalın kısa alt başlıklar ("**Tetikleyici:**", "**Paket yapısı:**", "**Ön çalışma ve fizibilite:**") + kısa paragraflar. Bağımsız/bağımlı değişkenler ve istatistiksel yöntemler ayrı maddelerde.
- Her şekil metinde önce anılır ("Şekil 3'te sunulmuştur."), sonra şekil gelir, sonra "Şekil 3'te görüldüğü gibi ..." ile açıklanır.

**Dil (yapay zekâ izini azaltmak için)**
- Kısa, düz cümleler; bir cümlede tek iddia. Öğrenci ama yetkin bir dil.
- Kaçın: uzun parantez içi ayrıntılar, noktalı virgülle zincirlenmiş listeler, "(i), (ii), (iii)" numaralandırmaları, kısaltma yığınları, kanun/plan paragraf numaralarının sıralanması, "kritik", "doğrudan örtüşmektedir", "uçtan uca", "kapsamlı" gibi süs sözcükleri, uzun tire ile cümle bağlama.
- Teknik ayrıntı yalnızca gerekçe veriyorsa kalır (ör. "BLE yayın paketi 31 bayt olduğundan paket 26 bayttır"). Bayt tabloları, durum makineleri, standart alan eşlemeleri metne değil, gerekirse ek/teknik rapora.
- Klinik/aşırı iddia yok: ölçemediğin şeyi vaat etme (ör. skor "klinik triyaj" değil "arama öncelik skoru"; "metre altı konum" yok). Kapsam dışı olanları 5. bölümde tek paragrafta yaz.
- Örneklerdeki kalıplar: "Bu durum projenin motivasyonunu oluşturmaktadır.", "Proje kapsamında ... Şekil X'te sunulmuştur.", "Araştırmanın başarısına katkısı %X'tir."

**Kaynaklar**
- **30–40 kaynak**, metinde **[1], [2] numaralı** biçim, ilk geçiş sırasına göre. Girdi biçimi: Yazar, A., Yazar, B. (Yıl). Başlık. Dergi, Cilt(Sayı), sayfa. DOI: ...
- Önce geniş bir doğrulanmış **kaynak havuzu** kur (`uretim/kaynak_havuzu.md`), metinde yalnızca en güçlülerini kullan. Havuzdaki her kaynak doğrulanmış olmalı.
- Resmî belgeler için URL + erişim tarihi; Resmî Gazete için tarih ve sayı.

## 2. Kaynak doğrulama (MCP ile)

Kullanılan MCP sunucuları (Claude Code'a kurulu olmalı):

| Sunucu | Kurulum | Kullanım |
|---|---|---|
| paper-search-mcp | `claude mcp add paper-search-mcp -s user -- uvx --with "mcp<2" paper-search-mcp` | `get_crossref_paper_by_doi` (her DOI), `search_crossref`, `search_openalex`, `search_pubmed` (DOI'si olmayan/eksik kayıtlar) |
| arxiv | `claude mcp add arxiv -s user -- uvx arxiv-mcp-server` | arXiv ön baskıları (`get_abstract`, `search_papers`) |
| semantic-scholar | `claude mcp add semantic-scholar -s user -- uvx --python 3.13 --from git+https://github.com/akapet00/semantic-scholar-mcp semantic-scholar-mcp` | ilgili makale önerisi, `get_paper_details`, `export_bibtex` |
| context7 | (kurulu) | yalnızca kütüphane/API belgesi için; kaynak kontrolünde gerekmez |

Resmî sayfalar (AFAD, SBB, Resmî Gazete, KVKK, BTK, TÜBİTAK, Android belgeleri) için `WebFetch`; engellenirse `curl -sIL` ile HTTP durumu alınır ve "elle kontrol" diye işaretlenir. Zotero bu iş için gerekmez (kaynakça TYBS'ye düz metin girilir).

**Yöntem**
1. DOI listesini 2–3 parçaya böl ve paralel alt ajanlarla doğrula; her ajan sonucu JSON yazsın: `{k, doi, status: OK|MINOR|ERROR|NOT_FOUND, crossref_title, crossref_authors, crossref_year, container, volume, issue, page, issues[]}`.
2. Karşılaştırılan alanlar: başlık, yazar soyadları (sayı ve sıra), yıl, dergi, cilt, sayı, sayfa.
3. Yorumlama kuralları:
   - Çevrim içi yayın yılı ≠ sayı yılı → MINOR; künyede sayı yılı kalabilir.
   - Crossref'te sayfa/yazar eksik → MINOR ("doğrulanamadı"), hata değil.
   - Başlık yayımlandığı hâliyle yazılır (ör. "Turkey" ise "Türkiye" diye çevrilmez).
   - Çok kelimeli soyadlarına dikkat ("Curto Pelle", "Del Valle").
   - Crossref'te olmayan DOI'yi doi.org yönlendirmesiyle kontrol et (ör. 10.22037/aaem...).
4. Alt ajan bulgularından düzeltme gerektirenleri **kendin yeniden doğrula** (MCP + curl), sonra uygula.
5. Metin içi atıf ↔ kaynakça eşleşmesini betikle kontrol et: her kaynağa atıf var mı, atıfı olup kaynakçada olmayan var mı.
6. Çıktıları tarihli olarak `dogrulama_kayitlari/` altına kaydet (ret gerekçesi "kaynak doğruluğu" olabilir; kayıt saklanır).
7. Başvuru sahibi için tıklanabilir `DOI_tiklama_listesi.md` üret (ÜYZ rehberi gereği son kontrol insan tarafından yapılır).

## 3. Şekiller

**Tasarım dili:** düz tasarım (flat design) / düz vektör illüstrasyon, infografik tarzı. Gölge, gradyan, 3B yok; tek renk dolgular; basit ikonlar (telefon, enkaz, insan, baret, tablet, sinyal dalgası, üstü çizili baz istasyonu, pil, konum iğnesi); az yazı; renkler anlamlı (kırmızı acil, yeşil akış, mavi teknoloji). Örnek önerilerdeki stok fotoğraf/clipart yerine **kendi çizdiğimiz vektör ikonlar** (telif riski yok).

**Beş şekil türü** (örnek önerilerdeki dağılım):
1. Zihin haritası (XMind tarzı): siyah merkez düğüm, renkli ana dallar, soluk alt düğümler, kavisli bağlantılar → 1.1'de problem.
2. Sade veri grafiği → 1.1'de problemin sayısal kanıtı; altına "Kaynak: [1], [2], [3]. Şematik gösterim."
3. İkonlu süreç akışı (saat yönünde 4 adım, kalın siyah oklar, her adımda tek satır kalın açıklama) → 1.2 amaç.
4. Senaryo/sistem illüstrasyonu (sahne: zemin katmanı, bileşenler, renkli veri akış okları, kırmızı uyarı etiketleri) → Yöntem başı.
5. Küçük resimli blok şema (2 satır yılan akışı, kalın sarı oklar, her blokta küçük çizim + başlık + "İA1 · Ay 1–2" rozeti) → Yöntem, iş adımlarıyla eşleşir.

**Teknik:** Her şekil bir Python betiğiyle satır içi SVG'li HTML olarak üretilir ve headless Chrome ile 2x PNG alınır. Ortak yardımcılar `<beceri>/scripts/sekil/lib.py` içindedir (`text`, `rect`, ikonlar, `save`). `f1.py`–`f5.py` YAŞA projesinin beş şeklidir; yeni proje için bunları kopyalayıp içeriği değiştir. Çıktı klasörü çalışılan dizindeki `sekiller/` ya da `SEKIL_CIKTI` ortam değişkeni; Chrome yolu `CHROME` ortam değişkeniyle değiştirilebilir. Elle çalıştırma komutu:
```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 --window-size=1200,<H> --screenshot=<png> file:///<html>
```
Tuval 1200 px genişlik, Arial, etiketler kalın ve en az ~18 px. Her PNG'yi Read ile aç; üst üste binme, kırpılmış yazı varsa düzelt ve yeniden üret. Şekil başlığı "**Şekil n.** Açıklama" biçiminde, ortalı, şeklin altında.

## 4. Üretim hattı

Tüm komutlar proje kökünde çalıştırılır (gerekli: Python 3, `pip install python-docx`; PDF için Windows + Microsoft Word):
```
uretim/oneri_kaynak.md + uretim/kaynak_havuzu.md + proje.json
        │  python <beceri>/scripts/derle.py
        ▼
<AD>_oneri_metni.md, kaynaklar.md, <AD>_TYBS_metni_tam.md, DOI_tiklama_listesi.md
        │  python <beceri>/scripts/docx_uret.py      (python-docx; TÜBİTAK form kalıbı)
        ▼
<AD>_Arastirma_Onerisi.docx
        │  powershell -File <beceri>/scripts/pdf_uret.ps1 -Docx <AD>_Arastirma_Onerisi.docx
        ▼
<AD>_Arastirma_Onerisi.pdf
```
- `derle.py`: `[@anahtar]` → ilk geçiş sırasına göre `[n]`; anahtar → havuz girdisi eşlemesi `proje.json` içindeki `anahtarlar` sözlüğündedir; yeni kaynak eklerken önce havuza ekle, sonra sözlüğe anahtar ekle. Atıf almayan anahtarları çıktıda listeler.
- `docx_uret.py`: A4, Arial 9, logo, üst bilgi, formun italik açıklama metinleri, her bölüm tek hücreli çerçeveli kutu; şekiller ve tablolar kutunun içinde; 3.x ve 4 tabloları kutu dışında ve "(*)" notlarıyla; bütçe tablosu + NOT. `<!-- cols: 35,65 -->` yorumu tablo sütun yüzdeleridir.
- Metni **her zaman `uretim/oneri_kaynak.md` üzerinden** değiştir; üretilen .md/.docx dosyalarını elle düzenleme.
- PDF'yi `pymupdf` ile sayfa sayfa PNG'ye çevirip gözle kontrol et (boş sayfa, bölünmüş şekil, bozuk kalın işaretleri).

## 5. Son kontrol listesi

- [ ] Özet 25–450 kelime; 1.1, 1.2, Yöntem ≥ 350 karakter (betikle say).
- [ ] Takvim puanları toplamı 100; yasak iş adımı yok; süre ≤ 12 ay.
- [ ] Bütçe ≤ 12.000 TL; tablo ile TYBS ekranı aynı.
- [ ] Her kaynağa atıf var; DOI'li her kaynakta DOI var; doğrulama kaydı tarihli olarak kaydedildi.
- [ ] Marka adı yok; ÜYZ beyanı 5. bölümde ve TYBS alanında.
- [ ] Danışman unvanı, laboratuvar adları resmî yazımla aynı.
- [ ] Şekiller PNG (TYBS yalnızca .jpg/.jpeg/.png kabul eder) ve metinde sırayla anılıyor.
- [ ] docx kaynağın son hâlinden sonra üretildi (dosya saatlerini karşılaştır); PDF görsel olarak kontrol edildi.
- [ ] Commit yalnızca kullanıcı isterse.
