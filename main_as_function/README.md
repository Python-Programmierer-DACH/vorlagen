# main_as_function

Einfaches Script, welches euer Programm in eine Funktion kapselt und somit neben dem direkten Aufruf auch kontrolliert von einem anderen Programm importier- und aufrufbar ist.

Es kann direkt aufgerufen werden:

`python script.py`

oder als Modul von einem anderen Modul importiert und ausgeführt werden:
```python
from script import main  # Importiert die Funktion main aus script.py

main()  # Ruft die Funktion ohne Parameter auf
```

# Vorlagen

## [main_as_function_comments.py](main_as_function_comments.py)
Datei mit vollständigen Erklärungen in den Kommentaren.

## [main_as_function.py](main_as_function.py)
Reduzierte Datei ohne Kommentare, die man als Vorlage verwendet, sobald man die Methodik versteht.
