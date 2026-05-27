# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

"""
DECLARACION DE VARIABLES
"""

"""
PERSONAJES
"""
define g = Character("Gon", color="#D68F27")
define b = Character("Bulbby", color="#FFF62E")
define e3 = Character("Eileen", who_font="Roboto-Regular.ttf", what_font="Roboto-Light.ttf")
 
"""
TRANSFORMACIONES Y DEMAS COSAS
"""
# The game starts here.

label start:

    scene bg backrooms

    show bulbby hi at center
    with dissolve
            
    b "Yo yo yo... Wassuuup!"

    window show

    b "Aquí te muestro el menú, mostro."

label tutorials:

    show bulbby hi at left
    with move

    b "Coñete..."
    # This ends the game.

    return
