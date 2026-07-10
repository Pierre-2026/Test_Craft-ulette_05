"""
CraftCalc

Version : 0.2.0

Widgets graphiques personnalisés.
"""


import customtkinter as ctk



# --------------------------------------------------
# TITRE
# --------------------------------------------------

class TitleWidget(ctk.CTkLabel):
    """
    Titre principal de l'application.
    """


    def __init__(
        self,
        master,
        text
    ):

        super().__init__(

            master,

            text=text,

            font=(
                "Arial",
                28,
                "bold"
            )

        )



# --------------------------------------------------
# LIGNE COMPOSANT
# --------------------------------------------------

class ComponentWidget:
    """
    Ligne permettant de sélectionner
    un ingrédient.
    """



    def __init__(
        self,
        master,
        item_list,
        remove_callback
    ):


        self.frame = ctk.CTkFrame(
            master
        )


        self.frame.pack(

            fill="x",

            pady=5

        )



        # Liste des objets

        self.combo = ctk.CTkComboBox(

            self.frame,

            values=item_list,

            width=250

        )


        self.combo.pack(

            side="left",

            padx=10

        )


        if item_list:

            self.combo.set(
                item_list[0]
            )



        # Quantité

        self.quantity = ctk.CTkEntry(

            self.frame,

            width=70

        )


        self.quantity.insert(

            0,

            "1"

        )


        self.quantity.pack(

            side="left",

            padx=10

        )



        # Suppression

        self.delete_button = ctk.CTkButton(

            self.frame,

            text="X",

            width=40,

            command=lambda:
            remove_callback(
                self
            )

        )


        self.delete_button.pack(

            side="left",

            padx=10

        )



    def get_value(self):

        """
        Retourne :

        nom objet
        quantité
        """


        try:

            quantity = int(

                self.quantity.get()

            )

        except:

            quantity = 1



        return (

            self.combo.get(),

            quantity

        )



    def destroy(self):

        self.frame.destroy()



# --------------------------------------------------
# RESULTAT
# --------------------------------------------------

class ResultWidget(ctk.CTkFrame):
    """
    Affichage d'un résultat de craft.
    """



    def __init__(
        self,
        master
    ):


        super().__init__(
            master
        )


        self.label = ctk.CTkLabel(

            self,

            text="",

            font=(

                "Arial",

                18

            )

        )


        self.label.pack(

            padx=20,

            pady=20

        )



    def display(
        self,
        text
    ):


        self.label.configure(

            text=text

        )