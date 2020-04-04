# Vorlagen
Hier gibt es Vorlagen für neue Projekte für verschiedene Anwendungszwecken mit verschiedenen Ansätzen.

## Allgemeines

### Shebang
Benutze grundsätzlich einen "_shebang_" in der ersten Zeile deines Hauptprogrammes. Das ermöglicht auf Unix-basierten Betriebssystemen das direkte Ausführen des Scriptes mit dem vorgesehenen Interpreter. Auch wenn Python unter Windows benutzt wird, sollte man den Richtlinien folgen. Außerdem gibt es unter **Windows** auch Tools oder Gegebenheiten, die diese Zeile auswerten. Der Shebang ist für Python selber nur ein Kommentar durch die Raute und wird somit ignoriert.

| Erste Zeile | Beschreibung |
|----------------------------|-----------------------------------------------------------------------------------------|
| `#!/usr/bin/env python3`   | Beste Option. Es wird in der PATH-Umgebungsvariablen nach dem Programm python3 gesucht. |
| `#!/usr/bin/python3`       | Schlechtere Option. Benutzt den konkreten Python-Interpreter unter diesem Pfad. Python kann unter umständen dort bei jemandem nicht installiert sein: `bash: ./test.py: /usr/bin/python4: Defekter Interpreter: Datei oder Verzeichnis nicht gefunden` |
| `#!/usr/bin/env python2`   | Python 2 wird seit 2020 nicht mehr gepflegt und sollte nicht mehr verwendet werden.  |
| `#!/usr/bin/env python`    | `python` kann je nach Betriebssystem auf `python2` oder auf `python3` zeigen. Das Script sollte  dann auch mit beiden Versionen klar kommen. Das Betriebssystem Raspbian setzt beispielsweise leider primär immer noch auf Python2. |

Ein Shebang brauchen nur die Scripte, die direkt gestartet werden. Module, die per `import` eingebunden werden, benötigen keinen shebang.

Python-Dateien müssen für diese Methode ausführbar sein `chmod +x script.py` und *explizit* aufgerufen werden: `./script.py`. Zur Erklärung: Würde man `script.py` aufrufen, müsste das Script in den Pfaden der PATH-Variable auffindbar sein.

Der shebang wird letztendlich ignoriert, wenn der Python-Interpreter direkt mit dem Script gestartet wird: `python3 script.py`. Das Script muss in diesem Fall auch nicht ausführbar sein.

Unter Unix-Systemen werden Programme mit alternativen symbolischen Links (Verknüpfungen) aufgerufen.  
Beispiel mit Python:
```bash
ls -al /usr/bin/python*
lrwxrwxrwx 1 root root     7 21. Dez 21:57 /usr/bin/python -> python3
lrwxrwxrwx 1 root root     9 22. Okt 11:14 /usr/bin/python2 -> python2.7
-rwxr-xr-x 1 root root 14088 22. Okt 11:14 /usr/bin/python2.7
-rwxr-xr-x 1 root root  1681 22. Okt 11:14 /usr/bin/python2.7-config
lrwxrwxrwx 1 root root    16 22. Okt 11:14 /usr/bin/python2-config -> python2.7-config
lrwxrwxrwx 1 root root     9 21. Dez 21:57 /usr/bin/python3 -> python3.8
-rwxr-xr-x 1 root root 14088 21. Dez 21:57 /usr/bin/python3.8
-rwxr-xr-x 1 root root  3120 21. Dez 21:57 /usr/bin/python3.8-config
lrwxrwxrwx 1 root root    16 21. Dez 21:57 /usr/bin/python3-config -> python3.8-config
lrwxrwxrwx 1 root root    14 21. Dez 21:57 /usr/bin/python-config -> python3-config
```

Offizielle Ankündigung zu Python-Aufrufen unter Unix (PEP 394): https://www.python.org/dev/peps/pep-0394/

### Encoding
In der ersten oder zweiten Zeile kann und sollte die Textkodierung angegeben werden:  
`# -*- coding: utf-8 -*-`

UTF-8 ist ein guter internationaler Standard gegenüber alten Ascii-Kodierungen, die nur auf einem Byte basieren. Mit UTF-8 werden Sonderzeichen und Umlaute bishin zu chinesischen Zeichen richtig interpretiert. Natürlich muss der Editor, mit dem die Datei erstellt oder bearbeitet wird, auch mit UTF-8 arbeiten.

Programme wie Notepad++ zeigen die Kodierung an und können sie ggf. konvertieren.

Offizielle Ankündigung zum Encoding (PEP 263): https://www.python.org/dev/peps/pep-0263

### Sontiges
Bei OpenSource-Projekten sollte in jeder Datei ein Hinweis auf die Lizenz vorliegen, unter der das Script geschrieben wurde.

Autor, zugehöriges Projekt und Internet-Adresse des Projektes lassen die Datei nicht alleine im Dunkeln stehen. Dazu sollte man spezielle Variablen nutzen, die auch direkt von Dokumentations-Software automatisch interpretiert wird:
```python
__author__ = "Max Mustermann"
__copyright__ = "Copyright 2020, Mein Projekt"
__license__ = "GPL"
__version__ = "1.0.1"
```
Die Version kann auch im Programm aktiv abgefragt werden, wenn Programmteile eine abweichende Version und inkompatibel sein könnten.

## Fertige Vorlagen

### [main_as_function](main_as_function/README.md)
Einfaches Script, welches euer Programm in eine Funktion kapselt und somit neben dem direkten Aufruf auch kontrolliert von einem anderen Programm importier- und aufrufbar ist.

### [main_as_class](main_as_class/README.md)
Der objektorientierte aber einfache Ansatz, der euer Programm auch von anderen Stellen mehrfach unabhängig aufrufbar macht.

### PyQt5
`#TODO`
