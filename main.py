"""
CraftCalc

Version : 0.3.0

Point d'entrée du programme.
"""


from gui import CraftCalculator



def main():


    try:

        app = CraftCalculator()

        app.run()


    except Exception as error:


        print(
            "Erreur CraftCalc :"
        )

        print(error)



        input(
            "\nAppuyez sur Entrée pour fermer..."
        )




if __name__ == "__main__":

    main()