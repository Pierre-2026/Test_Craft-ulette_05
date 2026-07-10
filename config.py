"""
CraftCalc

Version : 0.3.0

Configuration générale du logiciel.
"""

import os
import sys



# ==================================================
# CHEMIN APPLICATION
# ==================================================

def get_application_path():

    """
    Retourne le dossier où se trouve l'application.

    Compatible :
    - mode développement Python
    - PyInstaller (.exe)
    """


    if getattr(
        sys,
        "frozen",
        False
    ):

        return os.path.dirname(
            sys.executable
        )


    return os.path.dirname(
        os.path.abspath(__file__)
    )




BASE_DIR = get_application_path()



# ==================================================
# DOSSIERS
# ==================================================

DATA_DIR = os.path.join(

    BASE_DIR,

    "data"

)



IMAGE_DIR = os.path.join(

    BASE_DIR,

    "images"

)



# ==================================================
# FICHIERS DONNEES
# ==================================================

ITEMS_FILE = os.path.join(

    DATA_DIR,

    "items.csv"

)



RECIPES_FILE = os.path.join(

    DATA_DIR,

    "recettes.csv"

)



# ==================================================
# APPLICATION
# ==================================================

APP_NAME = "CraftCalc"



VERSION = "0.3.0"



# ==================================================
# FENETRE
# ==================================================

WINDOW_WIDTH = 700

WINDOW_HEIGHT = 750



# ==================================================
# THEME
# ==================================================

THEME_MODE = "dark"


THEME_COLOR = "blue"



# ==================================================
# OPTIONS
# ==================================================

DEBUG = True