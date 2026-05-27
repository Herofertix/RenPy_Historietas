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

    show gon frick at center
            
    g "Fuck you you look like a looooooser... Frick you! (With care)"

    show gon frick
    
    show bulbby hi at right

    b ":,("
    
    b "You are a the looser... Bitch"

    e3 "Similarly, the who_font and what_font properties set the font used by the different kinds of text."
    # This ends the game.

    return
