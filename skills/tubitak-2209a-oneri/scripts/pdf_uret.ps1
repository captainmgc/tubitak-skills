# <AD>_Arastirma_Onerisi.docx -> .pdf (Microsoft Word ile, yalnızca Windows)
# Çalıştırma: powershell -File <beceri>/scripts/pdf_uret.ps1 -Docx <yol>.docx
param([Parameter(Mandatory = $true)][string]$Docx)
$giris = (Resolve-Path $Docx).Path
$cikti = [IO.Path]::ChangeExtension($giris, '.pdf')
$w = New-Object -ComObject Word.Application; $w.Visible = $false
try {
    $doc = $w.Documents.Open($giris, $false, $true)
    $doc.ExportAsFixedFormat($cikti, 17)
    "sayfa: " + $doc.ComputeStatistics(2)
    $doc.Close($false)
} finally { $w.Quit() }
