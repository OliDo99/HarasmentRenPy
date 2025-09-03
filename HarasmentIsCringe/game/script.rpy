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
        if not povname:
         povname = "You"
        player_score = 100

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
            python:
                player_score += 10 
            jump intervene_route
        "Pretend you know Silvie":
            python:
                player_score += 10 
            jump silvie_route
        "Ignore":
            python:
                player_score -= 10
            jump ignore_route
            
                    

label intervene_route:
    
    scene bg street
    show man body
    
    pov "Hey!"
    show man talking
    m "Mind your own business!"
    show man body 
    menu:
        "Talk to him":
            python:
                player_score += 10 
            jump talk_route
        "Punch him":
            python:
                player_score -= 10 
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
    scene bg street night
    
    "You left"
    "You never saw her again"

    scene bg black
    centered "If you see a questionable situation, it's always better to make sure everything is alright, rather than ignore it. Better safe than sorry"

    jump second_chapter

label silvie_route:
    show man body at left
    show silvie body at right
    pov "Hey! There you are, I've been looking all over for you."
    pov "Are you ready to go?"
    show silvie answering at right
    s "uhhh..."
    s "Yeah, thanks lets go"

    scene bg black
    centered "Pretending to know the person being harassed can be a good and subtle way to make sure they are feeling safe without alerting the perpetrator"
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
            python:
                player_score += 10 
            jump concerned_route2
        "Intervene":
            python:
                player_score -= 10 
            jump intervene_route2
        "Explain it yourself":
            python:
                player_score += 10 
            jump explain_route2
        "Observe":
            python:
                player_score += 10 
            jump ignore_route2

label intervene_route2:
    pov "Hey! Leave her alone!"
    show man asking at left
    m "What? I was just asking for help. I got this card yesterday and I don't know how it works"
    show silvie answering at right
    s "I was just showing him how to use it, I'm fine"
    pov "Oh, sorry for interrupting"

    scene bg black
    centered "Not all situations are dangerous, try to take a subtle approach to measure the situation before trying to intervene"

    jump third_chapter

label ignore_route2:
    scene bg train
    show man body at left
    show silvie answering at right
    "You decide to do nothing and oberve the situation"
    s "You press it here like this until you hear a sound"
    show silvie body at right
    show man asking at left
    m "Thanks, you are a life saver"

    scene bg black
    centered "Sometimes, taking a step back and judging the situation is better than rushing in"

    jump third_chapter

label concerned_route2:
    scene bg train
    show man body at left
    show silvie body at right
    pov "Is everything alright here?"
    s "Yeah I was just showing this man how to use OV"
    m "Thank you, I don't know how this card worked and no one was willing to help so far"

    scene bg black
    centered "Calmly approaching a quetionable situation and checking up can be a good way to make sure everything is alright"

    jump third_chapter

label explain_route2:
    scene bg train
    show man asking at left
    show silvie body at right
    pov "I can show you, you just tap it on that scanner"
    m "Thanks, you are a life saver"

    scene bg black
    centered "Offering help in a seemingly normal situation can be a good ay to make sure both parties are safe"



label third_chapter:
    scene bg street

#Person A walking past Person B 
    show laura body at right
    show man talking at left

    m "Hey girl! Lookin' good in that dress!" 
    show man body at left
    l "..."
    show man talking at left
    m "Damn, don't ignore me! I'm giving you a compliment!" 
    show laura fuck off

    l "I’m not interested. Please leave me alone." 
    show laura body flip

    m "Wow, calm down! No need to be such a bitch about it. I was just being nice." 
    show man body

    menu:
        "Make fun of him":
            jump embarrassing_route3
        "Intervene":
            python:
                player_score += 10 
            jump intervene_route3
        "Ignore":
            python:
                player_score += 10 
            jump ignore_route3

label embarrassing_route3:
    pov "Mate, this isn't working. Try therapy next time."
    m "Fuck you, man. All chicks are the same anyway"
    jump end_chapter

label intervene_route3:
    pov "Hey man, she's not interested!"
    show man whatever
    m "Whatever. Can’t even say hi to people these days." 

    menu:
        "Calm approach":
            python:
                player_score += 10 
            jump calm_intervene_route3
        "Be sarcastic":
            python:
                player_score += 10 
            jump sarcastic_intervene_route3
        "Ignore":
            python:
                player_score -= 10 
            jump end_chapter


    #Person A walks away while Person B talking to bystander 
label ignore_route3:
    scene bg street
    show man groping
    show laura body flip at right
    l "Get away from me!"
    jump end_chapter

label calm_intervene_route3:
    pov "This isn’t saying hi, it's harassment. Walk away, or I'll get security."
    m "Tch. Whatever."
    jump end_chapter

label sarcastic_intervene_route3:
    pov "Oh wow, thanks for blessing us with your unsolicited opinion. Shall we share it with your mother?"
    m "Whatever. You're so boring"
    jump end_chapter

    


label end_chapter:
    "The End"
    return
