# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Silvie", color="#c8ffc8")
define l = Character("Laura", color="#8e4efe")
define m = Character("Boyle", color="#ff8818")
define cop = Character("Police", color="#ff0000c1")
define pov = Character("[povname]", color="#28ff10")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg classroom

    "Welcome to our Pressure Cooker game about street harassment!"
    "In this game, you will be presented with different scenarios where you can choose to either to intervene or ignore street interactions."
    "Your choices will affect your social credit score, so choose wisely!"
    

    python:
        povname = renpy.input("Before we start, what is your name?", length=32)
        povname = povname.strip()
        player_score = 0

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


label first_chapter:
    scene bg street
    show man talking at left
    show silvie body at right

    # These display lines of dialogue.
    m "Hello sweetheart, you look so good today!"
    show man body at left
    show silvie anoyed at right
    s "Sorry?"
    show silvie body at right
    show man talking at left
    m "Dont be like that baby"

    m "Come on, just give me a chance"
    show man body at left
    show silvie anoyed at right
    s "Leave me alone!"
    show silvie body at right
    show man talking at left
    m "Why? You dont want to have fun?"
    show man body at left


    menu:
        "Intervene":
            jump intervene_route
        "Ignore":
            jump ignore_route

label intervene_route:
    "+10 social credit score"
    scene bg street
    show man body

    pov "Hey!"
    show man talking
    m "Mind your own business!"
    show man body 
    menu:
        "Talk to him":
            jump talk_route
        "Pretend you know Silvie":
            jump silvie_route
        "Punch him":
            jump fight_route

label talk_route:
    pov"Could you please leave her alone?"
    show man talking
    m"What? Why?"
    show man body
    pov "Forcing yourself on someone is harassment and it's not okay"
    show man talking
    m "I didn't mean it like that, but fine I'll leave"
    
    scene bg black
    centered "You did the right thing, calmly explaining the situation without escalating is always the best approach"


    jump second_chapter

label fight_route:
    pov "Hey back off man! Take this!"
    "You punch him in the face"
    show man grabbing
    m "Ouch! You bastard..."
    show man knife
    "He pulls out a knife"
    
    m "Now you've done it!"
    show cop body at left
    cop "Drop the knife!"
    "The cops arrest both of you"

    scene bg black
    centered "Violence is never the answer, you should always try to de-escalate the situation first"
    
    jump second_chapter

label ignore_route:
    "-10 social credit score"
    scene bg street night
    with fade
    
    "You left"
    "You never saw her again"

    jump second_chapter

label silvie_route:
    scene bg street night
    jump second_chapter


label second_chapter:
    scene bg station
    show man asking at left
    show silvie body at right

    # These display lines of dialogue.
    m "Hey, can you show me how to use the OV chipkaart?"
    show man body at left
    show silvie answering at right
    s "Oh you just scan it when you get on a bus or train"
    show silvie body at right
    show man talking at left
    m "Could you show me?"
    show man body at left

    menu:
        "Everything alright?":
            jump concered_route2
        "Intervene":
            jump intervene_route2
        "Explain OV":
            jump explain_route2
        "Ignore":
            jump ignore_route2

label intervene_route2:
    pov "Hey! Leave her alone!"
    show man asking at left
    m "What?"
    show silvie answering at right
    s "What hey, I was just helping him"
    pov "Oh, sorry"
    "-10 social credit score"
    jump third_chapter

label ignore_route2:
    scene bg train
    show man body at left
    show silvie answering at right
    s "You press it here like this"
    show silvie body at right
    show man asking at left
    m "Thanks, you are a life saver"

    jump third_chapter

label concerned_route2:
    scene bg train
    show man body at left
    show Silvie
    pov "Is everything alright here?"
    s "Yeah I was just showing this man how to use OV"

    jump third_chapter

label explain_route2:
    scene bg train
    show man asking at left
    show silvie body at right
    pov "I can show you, you just tap it on that scanner"
    m "Thanks, you are a life saver"



label third_chapter:
    scene bg street

#Person A walking past Person B 
    show laura body at right
    show man talking at left

    m "Hey girl! Lookin' good in that dress!" 
    show man body at left
    l "..."
    show man talking at left
    m "Damn, don't ignore me! I'm just giving you a compliment!" 
    show laura fuck off

    l "I’m not interested. Please leave me alone." 
    show laura body flip

    m "Wow, calm down! No need to be such a bitch about it. I was just being nice." 
    show man body

    menu:
        "Intervene":
            jump intervene_route3
        "Ignore":
            jump ignore_route3

label intervene_route3:
    pov "Hey man, she's not interested!"
    "+10 social credit"
    show man whatever
    m "Whatever. Can’t even say hi to people these days." 

    menu:
        "Calm approach":
            jump calm_intervene_route3
        "Be sarcastic":
            jump sarcastic_intervene_route3
        "Ignore":
            jump end_chapter


    #Person A walks away while Person B talking to bystander 
label ignore_route3:
    scene bg street
    show man groping
    show laura body flip at right
    "boob squeeze"
    jump end_chapter

label calm_intervene_route3:
    pov "This isn’t saying hi, it's harassment. Walk away, or I'll get security."
    m "Tch. Whatever."
    jump end_chapter

label sarcastic_intervene_route3:
    pov "Oh wow, thanks for blessing us with your unsolicited opinion. Shall we share it with your mother?"
    m "You chicks are all the same. Whatever."
    jump end_chapter

    


label end_chapter:
    "The End"
    return
