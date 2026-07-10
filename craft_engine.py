"""
CraftCalc

Version : 0.2.0

Moteur de fabrication.
"""

from models import Item, Recipe



class CraftEngine:
    """
    Gère toute la logique de craft.
    """


    def __init__(
        self,
        items,
        recipes
    ):

        self.items = items

        self.recipes = recipes



    # --------------------------------------------------
    # RECHERCHE DE RECETTES
    # --------------------------------------------------

    def find_recipes(
        self,
        resources
    ):

        """
        Recherche toutes les recettes possibles.

        resources :

        {
            id_item: quantité
        }

        Exemple :

        {
            1:3,
            2:2
        }

        """

        results = []


        for recipe in self.recipes:


            if self.can_craft(
                recipe,
                resources
            ):

                item = self.items.get(
                    recipe.result
                )


                if item:

                    results.append(item)



        return results



    # --------------------------------------------------
    # VERIFICATION
    # --------------------------------------------------

    def can_craft(
        self,
        recipe,
        resources
    ):

        """
        Vérifie si une recette est réalisable.
        """


        for item_id, needed in recipe.ingredients.items():


            available = resources.get(
                item_id,
                0
            )


            if available < needed:

                return False



        return True



    # --------------------------------------------------
    # RESSOURCES MANQUANTES
    # --------------------------------------------------

    def missing_resources(
        self,
        recipe,
        resources
    ):

        """
        Retourne les ressources manquantes.
        """


        missing = {}


        for item_id, needed in recipe.ingredients.items():


            available = resources.get(
                item_id,
                0
            )


            if available < needed:

                missing[item_id] = (
                    needed - available
                )



        return missing



    # --------------------------------------------------
    # DESCRIPTION RECETTE
    # --------------------------------------------------

    def recipe_description(
        self,
        recipe
    ):

        """
        Transforme une recette en texte lisible.
        """


        text = ""


        for item_id, quantity in recipe.ingredients.items():


            item = self.items.get(
                item_id
            )


            if item:

                text += (
                    f"{item.name} x{quantity}\n"
                )



        return text



    # --------------------------------------------------
    # FABRICATION MULTIPLE
    # --------------------------------------------------

    def max_craft_possible(
        self,
        recipe,
        resources
    ):

        """
        Calcule combien de fois une recette
        peut être réalisée.
        """


        maximum = None


        for item_id, needed in recipe.ingredients.items():


            available = resources.get(
                item_id,
                0
            )


            possible = (
                available // needed
            )


            if maximum is None:

                maximum = possible

            else:

                maximum = min(
                    maximum,
                    possible
                )



        return maximum or 0