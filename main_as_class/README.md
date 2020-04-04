# main_as_class

Erweitertes Script, welches euer Programm in eine Klasse kapselt und somit neben dem direkten Aufruf auch kontrolliert und mehrfach von einem anderen Programm importier- und aufrufbar ist.

Objektorientierte Programmierung bietet die beste Strukturierung von Funktionen, Namensräumen und Daten.

Das Script kann direkt aufgerufen werden:

`python script.py`

oder als Modul von einem anderen Modul importiert, instanziert und ausgeführt werden:
```python
from script import App  # Importiert die App-Klasse aus script.py
app = App()  # Erstellt eine Instanz von App in app
app.main()  # Ruft die Funktion main der Klasseninstanz app ohne Parameter auf
```

# Vorlagen

## [main_as_class_comments.py](main_as_class_comments.py)
Datei mit vollständigen Erklärungen in den Kommentaren.

## [main_as_class.py](main_as_class.py)
Reduzierte Datei ohne Kommentare, die man als Vorlage verwendet, sobald man die Methodik versteht.
