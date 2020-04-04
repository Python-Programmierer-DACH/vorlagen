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
    Was macht diese Klasse oder was stellt sie dar?
    """

    def __init__(self):
        """
        Creates an instance.
        """

        # Variablen bezogen auf die Instanz nur hier in "self" definieren.

    def main(self, *args: tuple, **kwargs: dict) -> int:
        """
        Was macht die main-Funktion?

        :param args: List of arguments from command line call.
        :param kwargs: Keyword args, when provided and called from an other module.
        :return: Exit code. 0 is success.
        """

        # Dein Code hier

        return 0

if __name__ == "__main__":
    try:
        myApp = MyApp()
        myApp.main()
        exitcode = myApp.main(*sys.argv[1:])
        sys.exit(exitcode)

    except Exception as e:
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        sys.exit(1)
