#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Was macht dieses Modul?
"""

import sys


def main(*args: tuple, **kwargs: dict) -> int:
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
        exitcode = main(*sys.argv[1:])
        sys.exit(exitcode)

    except Exception as e:
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        sys.exit(1)
