# NSBMD PNG Pipeline Tool - Mega Ultra Edition 😎

## Übersicht

Dieses Tool ermöglicht es, **NSBMD-Dateien** (z. B. `w1.nsbmd`) für **New Super Mario Bros. DS** zu bearbeiten, indem die Texturen als PNG exportiert, bearbeitet (z. B. mit **Tinke**) und anschließend wieder in die NSBMD importiert werden.  
Das Tool enthält epische ASCII-Banner, Dummy-Layer, Slow-Prints, Farbanimationen, Random Events und Backups für maximalen Coolness-Faktor.

---

## Features

- Automatischer Export der NSBMD-Bitmaps in PNG-Dateien  
- Vorbereitung der PNGs zur Bearbeitung in Tinke oder anderen Grafiktools  
- Import bearbeiteter PNGs zurück in NSBMD  
- Backups der Originaldateien  
- Epische ASCII-Banner, Ladeanimationen und Farbausgabe  
- Random Events und Easter Eggs für Spaß und epische Länge  
- Vollständig automatisierte Ordnererstellung (`map`, `png`, `finished`)

---

## Installation

1. **Python 3.10 oder höher** installieren:  
   [Python Download](https://www.python.org/downloads/)

2. **Benötigte Bibliothek installieren**:  
   Öffne CMD oder PowerShell und gib ein:
   ```powershell
   pip install pillow
Code speichern:
Speichere das Python-Script als nsbmd_pipeline_final.py.

Ordnerstruktur
Das Tool legt Ordner automatisch an, du musst nur die Dateien einfügen:

scss
Code kopieren
map       ← Original NSBMD-Datei(en) hier rein
png       ← Bearbeitete PNGs hier rein (nach Tinke)
finished  ← Fertige NSBMD-Datei wird hier abgelegt
Hinweis:

map muss mindestens die Original w1.nsbmd enthalten, sonst kann das Tool nichts exportieren.

png wird erst relevant, nachdem die PNGs in Tinke bearbeitet wurden.

Nutzung
Script ausführen:

powershell
Code kopieren
cd Pfad\zum\Script
python nsbmd_pipeline_final.py
ASCII-Banner & Dummy-Layer werden angezeigt.

PNGs im Ordner png mit Tinke bearbeiten.

Wenn die PNGs fertig sind, Enter drücken.

Das Tool packt die PNGs automatisch zurück in die NSBMD.

Fertige NSBMD-Datei befindet sich im Ordner finished, z. B.:

Code kopieren
finished\w1_mega_fixed_4.nsbmd
Tipps für Tinke
Stelle sicher, dass das PNG im richtigen TEX0/TEX1-Format gespeichert wird.

Originalauflösung & Pixelgröße nicht verändern, sonst kann NSMBe abstürzen.

Nutze Tinke nur für die Bildbearbeitung, das Script übernimmt das Zurückpacken in NSBMD.

Hinweise & Warnungen
Das Tool verändert die NSBMD-Datei, daher vorher immer Backup erstellen.

Wenn PNGs falsch formatiert sind, kann NSMBe abstürzen.

Dummy-Layer, ASCII-Banner, Slow-Prints, Farbausgaben und Random Events dienen nur zur epischen Länge und Coolness – sie beeinflussen den Import nicht.

Support / Probleme
Falls das Tool die PNGs nicht findet: Prüfe, dass die Dateien im richtigen Ordner png liegen.

Fehlermeldungen zu Python-Paketen: Stelle sicher, dass Pillow installiert ist.

Bei Crashs: Prüfe die PNG-Größe, Auflösung und TEX0/TEX1-Format.

Lizenz
Dieses Tool ist kostenlos für den privaten Gebrauch.
Keine Garantie auf Kompatibilität mit NSMBe, Tinke oder ROMs.
Benutzung auf eigene Verantwortung.

Fun Facts 😎
Mega ASCII-Banner beim Start

Random Events & Easter Eggs

Epische Ladeanimationen mit Dummy-Layern

Viel Spaß beim Modden deiner NSBMD-Dateien!
