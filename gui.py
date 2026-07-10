"""
CraftCalc

Version : 0.3.0

Interface graphique principale.
"""


import customtkinter as ctk


from config import (
    APP_NAME,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    THEME_MODE,
    THEME_COLOR,
    ITEMS_FILE,
    RECIPES_FILE
)


from csv_loader import (
    load_items,
    load_recipes
)


from craft_engine import CraftEngine


from widgets import (
    TitleWidget,
    ComponentWidget,
    ResultWidget
)


from utils import (
    find_item_by_name,
    safe_int,
    format_item_list
)



class CraftCalculator:
    """
    Fenêtre principale CraftCalc.
    """



    def __init__(self):


        # ------------------------------------------
        # Chargement données
        # ------------------------------------------

        self.items = load_items(
            ITEMS_FILE
        )


        self.recipes = load_recipes(
            RECIPES_FILE
        )


        self.engine = CraftEngine(
            self.items,
            self.recipes
        )



        self.components = []



        # ------------------------------------------
        # Configuration interface
        # ------------------------------------------

        ctk.set_appearance_mode(
            THEME_MODE
        )


        ctk.set_default_color_theme(
            THEME_COLOR
        )



        # ------------------------------------------
        # Fenêtre
        # ------------------------------------------

        self.window = ctk.CTk()


        self.window.title(
            APP_NAME
        )


        self.window.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
        )



        self.create_interface()



    # ==================================================
    # CREATION INTERFACE
    # ==================================================

    def create_interface(self):


        title = TitleWidget(

            self.window,

            "CRAFT CALCULATOR"

        )


        title.pack(
            pady=20
        )



        # Zone composants

        self.components_area = ctk.CTkScrollableFrame(

            self.window,

            width=620,

            height=350

        )


        self.components_area.pack(

            padx=20,

            pady=10

        )



        # Bouton ajout

        add_button = ctk.CTkButton(

            self.window,

            text="+ Ajouter un composant",

            command=self.add_component

        )


        add_button.pack(
            pady=5
        )



        # Bouton craft

        craft_button = ctk.CTkButton(

            self.window,

            text="FABRIQUER",

            height=40,

            command=self.search_craft

        )


        craft_button.pack(
            pady=10
        )



        # Résultat

        self.result = ResultWidget(

            self.window

        )


        self.result.pack(

            pady=15

        )



        # Deux composants par défaut

        self.add_component()

        self.add_component()



    # ==================================================
    # AJOUT COMPOSANT
    # ==================================================

    def add_component(self):


        component = ComponentWidget(

            self.components_area,

            format_item_list(
                self.items
            ),

            self.remove_component

        )


        self.components.append(
            component
        )



    # ==================================================
    # SUPPRESSION
    # ==================================================

    def remove_component(
        self,
        component
    ):


        if component in self.components:

            self.components.remove(
                component
            )


        component.destroy()



    # ==================================================
    # RECHERCHE CRAFT
    # ==================================================

    def search_craft(self):


        resources = {}



        for component in self.components:


            name, quantity = component.get_value()



            item = find_item_by_name(

                self.items,

                name

            )



            if item:


                if item.id in resources:

                    resources[item.id] += quantity


                else:

                    resources[item.id] = quantity




        results = self.engine.find_recipes(

            resources

        )



        if not results:


            self.result.display(

                "Aucun objet fabriquable"

            )


            return




        text = "Objets fabriquables :\n\n"



        for item in results:


            text += (

                f"• {item.name}\n"

            )



        self.result.display(

            text

        )



    # ==================================================
    # LANCEMENT
    # ==================================================

    def run(self):

        self.window.mainloop()