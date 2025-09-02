# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Silvie", color="#c8ffc8")
define m = Character("Boyle", color="#ff8818")
define pov = Character("Chad", color="#28ff10")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg street

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show man body at left
    show eva body at right

    # These display lines of dialogue.
    m "Hello sweetheart, you look so good today!"

    s "Hello?"

    m "Dont be like that baby"

    menu:
        "Intervene":
            jump intervene_route
        "Ignore":
            jump ignore_route



label intervene_route:
    
    scene bg street night
    with fade

    "+10 social credit score"
    show man body
    pov "Hey! Leave her alone!"
    m "Mind your own business!"
    pov "No! You shouldnt be harassing people like that!"
    m "What?? I didn't know that"
    jump end_chapter

label ignore_route:
    "-100 social credit score"
    scene bg street night
    with fade
    "He rapes her"
    jump end_chapter

label end_chapter:
    "The End"
    return
