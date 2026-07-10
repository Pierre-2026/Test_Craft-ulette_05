"""
CraftCalc

Version : 0.2.0

Modèles de données du logiciel.
"""


# --------------------------------------------------
# ITEM
# --------------------------------------------------

class Item:
    """
    Représente un objet utilisable dans le jeu.

    Exemple :
    Bois, Pierre, Hache en pierre...
    """


    def __init__(
        self,
        id,
        name,
        category,
        icon=None,
        description=""
    ):

        self.id = id

        self.name = name

        self.category = category

        self.icon = icon

        self.description = description



    def __str__(self):

        return self.name



    def to_dict(self):

        return {

            "id": self.id,

            "nom": self.name,

            "type": self.category,

            "icon": self.icon,

            "description": self.description

        }



# --------------------------------------------------
# RECIPE
# --------------------------------------------------

class Recipe:
    """
    Représente une recette de fabrication.

    Exemple :

    Bois x3
    Pierre x2

    donne :

    Hache
    """


    def __init__(
        self,
        id,
        ingredients,
        result
    ):


        self.id = id

        self.ingredients = self.parse_ingredients(
            ingredients
        )

        self.result = result



    # ----------------------------------------------
    # Conversion CSV
    # ----------------------------------------------

    def parse_ingredients(
        self,
        data
    ):

        """
        Transforme :

        1x3,2x2

        en :

        {
            1:3,
            2:2
        }
        """


        ingredients = {}


        if not data:

            return ingredients



        elements = data.split(",")


        for element in elements:


            item_id, quantity = element.split("x")


            ingredients[
                int(item_id)
            ] = int(quantity)



        return ingredients



    def __str__(self):

        return f"Recipe {self.id}"



    def to_dict(self):

        return {

            "id": self.id,

            "ingredients": self.ingredients,

            "result": self.result

        }