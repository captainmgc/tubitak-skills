# tubitak-skills

TÜBİTAK başvuruları için yapay zekâ kodlama ajanı becerileri (Claude Code, Cursor, Codex ve [skills](https://github.com/vercel-labs/skills) aracının desteklediği diğer ajanlar).

## Beceriler

| Beceri | Ne yapar |
|---|---|
| `tubitak-2209a-oneri` | 2209-A araştırma önerisi yazma ve sadeleştirme, MCP sunucularıyla kaynak/DOI doğrulama, düz tasarım (flat design) şekiller, TÜBİTAK form kalıbında docx/pdf üretimi |

## Kurulum

```bash
npx skills add captainmgc/tubitak-skills
```

Komut hangi ajana (Claude Code, Cursor vb.) ve nereye (bu proje / tüm projeler) kurulacağını sorar. Sorusuz kurmak için: `-a claude-code -y`, tüm projeler için ayrıca `-g`.

Kurduktan sonra ajana "2209-A önerisi yazalım", "kaynakları doğrula" ya da "örnek raporlara benzet" demeniz yeterli; Claude Code'da `/tubitak-2209a-oneri` ile de çağrılır.

## Gereksinimler

- Python 3 ve `pip install python-docx` (docx üretimi)
- Google Chrome (şekillerin PNG'ye çevrilmesi)
- PDF için Windows + Microsoft Word
- Kaynak doğrulama için MCP sunucuları: paper-search-mcp, arxiv-mcp-server, semantic-scholar-mcp (kurulum komutları `SKILL.md` içinde)

## Notlar

- Kabul almış örnek öneriler ve TÜBİTAK logosu repoya dahil değildir; kendi projenize siz eklersiniz.
- Çağrı kuralları 2026 çağrısına göredir; her yıl güncel çağrı duyurusunu kontrol edin.
- Kaynakların doğruluğundan başvuru sahibi sorumludur (TÜBİTAK ÜYZ rehberi).

## Lisans

MIT
