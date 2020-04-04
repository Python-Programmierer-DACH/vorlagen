#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dies ist ein Template für ein objektorientiertes und import-freundliches Script, welches auch Kommandozeilen-Argumente
ausliest.
Quelle: https://github.com/Python-User-Deutschland/vorlagen/blob/master/main_as_class/main_as_class.py
"""

import sys


class MyApp:
    """
    Ich bin ein Docstring für die Klasse MyApp.
    Die help-Funktion zeigt diesen Text hier an, indem der Aufruf und die Benutzung dieser Funktionen erklärt sein
    sollte.
    Unter Programmierern sollte man auch bei eingedeutschten Programmen dennoch auf Englisch schreiben.
    Das gilt für Hilfetexte, Kommentare und vor allem für Variabelennamen.
    """

    def __init__(self, instancename: str):
        """
        Hiermit wird (intern) eine Instanz der Klasse MyApp erstellt.
        Der Instanzname ist ein Beispiel.

        :param instancename: Name of this instance for identification.
        """

        # Alle Variablen und Werte bezogen auf die Instanz werden nur hier in "self" gespeichert.
        self.name = instancename  # Wir speichern den übergebenen Instanznamen.

        # Wir initialiieren ein paar Variablen
        self.title = "Meine App!"
        self.main_call_count = 0

    def welcome(self):
        """
        Ich bin ein Docstring.
        Die help-Funktion zeigt diesen Text hier an, indem der Aufruf und die Benutzung dieser Funktionen erklärt sein
        sollte.
        Unter Programmierern sollte man auch bei eingedeutschten Programmen dennoch auf Englisch schreiben.
        Das gilt für Hilfetexte, Kommentare und vor allem für Variabelennamen.
        Auch sollten in Docstrings von Funktionen immer die Parameter und der Rückgabewert der Funktion beschrieben werden.
        "self" ist die Referenz auf die Instanz, mit der man auf Variablen und Funktionen der Klasse bzw. deren
        Instanz zugreifen kann.

        Diese funktion schreibt eine individuelle Begrüßung auf die Konsole.
        """

        print(f"Hallo von der Instanz {self.name}, auch bekannt als {self.title}")

    def main(self, *args: tuple, **kwargs: dict) -> int:
        """
        Ich bin die Funktion main der Klasse MyApp.
        Ich verrichte die Hauptarbeit und heiße daher "main".
        """

        # Hier beginnt dein Programm im Prinzip
        # ============================================================

        # Funktionen innerhalb von Funktionen sind kein Problem und dienen
        # häufig der guten Strukturierung.
        def private_welcome():
            print("Die interne Funktion schreibt: Hallo Welt!")

        # Wir rufen eine normale Funktion dieser Klasse auf.
        # Da wir uns explizit auf diese Instanz beziehen, müssen wir "self" benutzen.
        self.welcome()

        private_welcome()  # So rufen wir unsere "interne" funktion auf.

        # Testweise alle gelistete Argumente und benannte Argumente ausgeben.
        for arg in args:
            print("Arg:", arg)

        for key, value in kwargs.items():
            print("Keyword", key, "=", value)

        # ============================================================
        # Hier ist dein Programm zu ende. Wenn alles geklappt hat, geben wir
        # nach fehlerfreier Ausführung die Erfolgsmeldung als Wert 0 zurück.
        return 0

if __name__ == "__main__":
    # Diese Abzweigung verhindert die unkontrollierte Ausführung deines
    # gesamten Moduls.
    # Diese Stelle wird nur ausgeführt, wenn diese Datei direkt gestartet wurde.
    #
    # Wenn andere Module dieses Modul importieren und nutzen wollen, müssen sie
    # in diesem Fall main() direkt aufrufen:
    #     from main_as_class import MyApp
    #     app = MyApp("Name der Instanz")
    #     app.main()
    # Es können auch Argumente an die Main-Funktion übergeben werden:
    #     app.main("arg1", "arg2", kwarg1=10, kwarg2="Hello World")

    # Wir achten auf mögliche Laufzeitfehler in unserem Programm.
    # Try-Blöcke sollten eigentlich gezielt für einzelne Zeilen angewendet werden.
    try:
        # Wir erstellen bzw. instanzieren eine "Kopie" unserer Klasse und benennen sie "Commandline".
        myApp = MyApp("Commandline")

        # Wir rufen eine Funktion auf. Das self der Funktion darf nicht angegeben werden. Es wird
        # intern automatisch mit übergeben.
        myApp.welcome()  # Wir rufen die Funktion "welcome" auf

        # Jezt starten wir die Hauptfunktion
        # Sie ruft unter anderem erneut das welcome() auf.
        # Das erste Argument in sys.argv ist der Scriptname. Der interessiert uns
        # nicht und wird direkt ausgefiltert.
        exitcode = myApp.main(*sys.argv[1:])

        # Der Aufruf hat zumindest ohne Laufzeitfehler geklappt.
        # Wir übergeben den Exitcode an den Aufrufer, damit er ggf. auf Fehler reagieren kann.
        sys.exit(exitcode)

    except Exception as e:
        # Es gab einen Laufzeitfehler und das Programm lief vermutlich nicht zu Ende durch.
        # Wir schreiben die erhaltene Fehlermeldung auf "stderr", dem Ausgabekanal für Fehlermeldungen.
        sys.stderr.write(str(e))
        sys.stderr.write("\n")

        # Wir übergeben den Fehlercode 1 an den Aufrufer, damit er ggf. auf Fehler reagieren kann.
        sys.exit(1)
