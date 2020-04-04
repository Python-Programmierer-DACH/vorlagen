#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dies ist ein Template für ein import-freundliches script, welches auch Kommandozeilen-Argumente ausliest.
Quelle: https://github.com/Python-User-Deutschland/vorlagen/blob/master/main_as_function/main_as_function.py
"""

import sys


def main(*args: tuple, **kwargs: dict) -> int:
    """
    Ich bin ein Docstring.
    Die help-Funktion zeigt diesen Text hier an, indem der Aufruf und die Benutzung dieser Funktionen erklärt sein sollte.
    Unter Programmierern sollte man auch bei eingedeutschten Programmen dennoch auf Englisch schreiben.
    Das gilt für Hilfetexte, Kommentare und vor allem für Variabelennamen.
    Auch sollten in Docstrings von Funktionen immer die Parameter und der Rückgabewert der Funktion beschrieben werden.
    
    Diese funktion schreibt die übergebenen args und kwargs auf die Konsole.
    
    :param args: List of arguments from command line call.
    :param kwargs: Keyword args, when provided and called from an other module.
    :return: Exit code. 0 is success.
    """

    # Hier beginnt dein Programm im Prinzip
    # ============================================================

    # Funktionen innerhalb von Funktionen sind kein Problem und dienen
    # häufig der guten Strukturierung.
    def welcome():
        "Ich bin die Funktion 'welcome' und grüße die Welt."
        print("Hello World!")

    welcome()  # Die eigene Funktion aufrufen

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
    #     from main_as_function import main
    #     main()
    # Es können auch Argumente an die Main-Funktion übergeben werden:
    #     main("arg1", "arg2", kwarg1=10, kwarg2="Hello World")

    # Wir achten auf mögliche Laufzeitfehler in unserem Programm.
    try:
        # Wir starten unser Programm in der main-Funktion und übergeben die
        # Kommandozeilen-Argumente direkt.
        # Das erste Argument in sys.argv ist der Scriptname. Der interessiert uns
        # nicht und wird direkt ausgefiltert.
        exitcode = main(*sys.argv[1:])

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
