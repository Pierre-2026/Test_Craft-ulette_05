"""
CraftCalc

Version : 0.2.0

Chargement des fichiers CSV.
"""


import csv
import os

from models import Item, Recipe



# --------------------------------------------------
# ITEMS
# --------------------------------------------------

def load_items(filename):

    items = {}


    if not os.path.exists(filename):

        raise FileNotFoundError(
            f"Fichier introuvable : {filename}"
        )


    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:


        reader = csv.DictReader(
            file,
            delimiter=";"
        )


        for row in reader:


            item = Item(

                id=int(row["id"]),

                name=row["nom"],

                category=row["type"]

            )


            items[item.id] = item



    return items




# --------------------------------------------------
# RECIPES
# --------------------------------------------------

def load_recipes(filename):

    recipes = []


    if not os.path.exists(filename):

        raise FileNotFoundError(
            f"Fichier introuvable : {filename}"
        )



    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:


        reader = csv.DictReader(
            file,
            delimiter=";"
        )



        for row in reader:


            recipe = Recipe(

                id=int(row["id"]),

                ingredients=row["ingredients"],

                result=int(row["resultat"])

            )


            recipes.append(recipe)



    return recipes