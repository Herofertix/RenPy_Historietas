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
define e = Character("Eileen", who_font="Roboto-Regular.ttf", what_font="Roboto-Light.ttf")
 
"""
TRANSFORMACIONES Y DEMAS COSAS
"""
# The game starts here.

init python:

    # A list of section and level objects.
    level_menu = [ ]

    class Section(object):
        """
        Represents a section of the level menu.

        `title`
            The title of the section. This should be a translatable string.
        """

        def __init__(self, title):
            self.kind = "section"
            self.title = title

            level_menu.append(self)


    class level(object):
        """
        Represents a label that we can jump to.
        """

        def __init__(self, label, title, move=True):
            self.kind = "level"
            self.label = label
            self.title = title

            if move and (move != "after"):
                self.move_before = True
            else:
                self.move_before = False

            if move and (move != "before"):
                self.move_after = True
            else:
                self.move_after = False

            level_menu.append(self)


    Section(_("Niveles"))

    level("backrooms", _("Backrooms"))


screen level_menu(adj):

    frame:
        xsize 640
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True
            draggable True

            vbox:
                for i in level_menu:

                    if i.kind == "level":

                        textbutton i.title:
                            action Return(i)
                            left_padding 20
                            xfill True

                    else:

                        null height 10
                        text i.title alt ""
                        null height 5

        bar adjustment adj style "vscrollbar"

        textbutton _("Ya está por hoy..."):
            xfill True
            action Return(False)
            top_margin 10


# This is used to preserve the state of the scrollbar on the selection
# screen.
default level_menu_adjustment = ui.adjustment()

# True if this is the first time through the level_menu.
default level_menu_first_time = True

# The game starts here.
#begin start
label start:
#end start

    scene bg washington
    show bulbby hi
    with dissolve

    window show

    b "Yeeeeeepa mostro!"

    b "Toma tus menús"

label level_menu:

    show bulbby hi at left
    with move

    call screen level_menu(adj=level_menu_adjustment)

    $ level = _return


    call expression level.label from _call_expression


    jump level_menu


    # Returning from the top level quits the game.
    return
