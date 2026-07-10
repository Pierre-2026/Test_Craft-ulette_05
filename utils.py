"""
CraftCalc

Version : 0.2.0

Fonctions utilitaires communes.
"""


import os
import sys



# --------------------------------------------------
# GESTION DES CHEMINS
# --------------------------------------------------

def get_base_path():

    """
    Retourne le dossier racine du programme.

    Fonctionne :
    - en mode développement Python
    - en version compilée PyInstaller (.exe)
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




def get_resource_path(
    relative_path
):

    """
    Retourne le chemin complet
    d'une ressource.

    Exemple :

    data/items.csv
    """


    return os.path.join(
        get_base_path(),
        relative_path
    )



# --------------------------------------------------
# CONVERSION
# --------------------------------------------------

def safe_int(
    value,
    default=1
):

    """
    Convertit une valeur en entier.

    Retourne default en cas d'erreur.
    """


    try:

        number = int(value)


        if number <= 0:

            return default


        return number


    except:

        return default




# --------------------------------------------------
# RECHERCHE OBJET
# --------------------------------------------------

def find_item_by_name(
    items,
    name
):

    """
    Recherche un objet par son nom.

    Retourne l'objet ou None.
    """


    for item in items.values():


        if item.name == name:

            return item



    return None



# --------------------------------------------------
# FORMATAGE
# --------------------------------------------------

def format_item_list(
    items
):

    """
    Retourne une liste de noms
    triée pour l'affichage.
    """


    names = [

        item.name

        for item in items.values()

    ]


    return sorted(
        names
    )



# --------------------------------------------------
# DEBUG
# --------------------------------------------------

def debug_message(
    message
):

    """
    Affichage debug centralisé.
    """


    print(
        f"[CraftCalc DEBUG] {message}"
    )