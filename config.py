"""
CraftCalc

Version : 0.2.0

Configuration générale du logiciel.
"""

import os


# --------------------------------------------------
# CHEMINS
# --------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)


IMAGE_DIR = os.path.join(
    BASE_DIR,
    "images"
)


ITEMS_FILE = os.path.join(
    DATA_DIR,
    "items.csv"
)


RECIPES_FILE = os.path.join(
    DATA_DIR,
    "recettes.csv"
)


# --------------------------------------------------
# INTERFACE
# --------------------------------------------------

APP_NAME = "CraftCalc"

WINDOW_WIDTH = 700

WINDOW_HEIGHT = 750


# --------------------------------------------------
# THEME
# --------------------------------------------------

THEME_MODE = "dark"

THEME_COLOR = "blue"


# --------------------------------------------------
# DEBUG
# --------------------------------------------------

DEBUG = True