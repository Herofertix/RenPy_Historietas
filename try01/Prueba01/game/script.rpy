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

"""
TRANSFORMACIONES Y DEMAS COSAS
"""

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg backrooms

    show gon frick at center
            
    "Gon" "Fuck you you look like a looooooser... Frick you! (With care)"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show gon frick
    transform move_slide:
        xalign 1.0 yalign 0.0
        linear 2.5 xalign 0.0
    show bulbby hi at right

    "Bulbby" ":,("
    
    "Bulbby" "You are a the looser... Bitch"

    # This ends the game.

    return
