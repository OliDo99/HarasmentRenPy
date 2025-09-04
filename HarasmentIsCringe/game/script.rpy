define s = Character("Silvie", color="#c8ffc8")
define l = Character("Laura", color="#8e4efe")
define m = Character("Boyle", color="#ff8818")
define cop = Character("Police", color="#ff0000c1")
define pov = Character("[povname]", color="#28ff10")





label start:

    scene bg classroom

    
    "Street harassment. It's an ugly reality."
    "We see it, we hear about it, but do we know what to do when we're face-to-face with it?"
    "In this game, you'll be a bystander. Your choices matter. Let's see how you handle the scenarios."

    python:
        povname = renpy.input("First, what should we call you?", length=32)
        povname = povname.strip()
        if not povname:
            povname = "You"
        player_score = 10 



label first_chapter:
    scene bg street
    show man talking at left
    show silvie body at right

    m "Hey, baby. You're looking amazing today."
    show man body at left
    show silvie anoyed at right
    s "Sorry... do I know you?" 
    show silvie body at right
    show man talking at left
    m "Not yet. But you could."
    m "Come on, give me a smile. It can't be that bad."
    show man body at left
    show silvie anoyed at right
    s "Please, just leave me alone." 
    show silvie body at right
    show man talking at left
    m "Whoa, whoa, what's the attitude for? I was just giving you a compliment." 
    show man body at left

    menu:
        "Intervene": 
            jump intervene_route
        "Pretend you know her": 

            jump silvie_route
        "Do nothing": 
            jump ignore_route

label intervene_route:

    menu:
        "Talk to him":
            jump talk_route
        "Punch him": 
            jump fight_route

label talk_route:
    pov "Hey man, I think she'd like to be left alone." 
    show man talking
    m "I'm just talking to her. What's it to you?"
    show man body
    pov "She looks uncomfortable. Just let it go, alright?"
    show man whatever
    m "Tch... whatever. Her loss."
    
    scene bg black
    centered "De-escalating is often the safest and most effective strategy. You focused on the behavior, not attacking him personally."
    jump second_chapter


label fight_route:
    pov "Back off! Or else—"

    "You swing and punch him."
    hide man body
    show man grabbing

    m "What the hell?!"

    show man knife
    show silvie scared 

    "He pulls out a knife"


    m "You’re dead, asshole!"

    show cop body at left
    "A patrol car was nearby and the police arrive quickly."
    show cop talking at left
    cop "Police! Break it up, both of you!"
    show cop yelling at left
    cop "Drop the knife now!"
    

    "The cops arrest both of you"
    hide man
    show cop talking
    cop"Are you okay, ma'am?"
    show silvie answering
    s "Y-yeah... thanks to you."


    scene bg black

    centered "Violence is never the answer, you should always try to de-escalate the situation first."



    jump second_chapter

label ignore_route:
    scene bg street night
    "You keep walking, trying not to make eye contact."
    "The sound of their voices fades behind you."
    "You'll never know how it ended."
    "But you never saw her again."

    scene bg black
    centered "Ignoring the situation is a choice—one that leaves the victim completely alone. Even a small distraction can help. A bystander's presence has power."
    jump second_chapter

label silvie_route:
    
    show man body at left
    show silvie body at right
    pov "Hey, Silvie! There you are, I was waiting for you." 
    pov "Sorry I'm late. You ready to go?"
    show silvie anoyed 
    s "Oh, uh..." 
    show silvie answering
    s "Yeah! Totally. Let's go."
    "She walks over to you, leaving the man standing there, confused."

    scene bg black
    centered "Creating a distraction by pretending to know the person is a safe and subtle way to remove them from a bad situation."
    jump second_chapter




label second_chapter:
    scene bg station
    show man asking at left
    show silvie body at right

   
    m "Excuse me? Sorry, I'm a bit lost. How do you use this... OV-chipkaart?" 
    show man body at left
    show silvie answering at right
    s "Oh, sure! You just have to tap it on the scanner when you get on or off."
    show silvie body at right
    show man talking at left
    m "Ah, I see. Could you maybe show me? I don't want to mess it up." 
    show man body at left

    menu:
        "Ask if everything is okay":
            jump concerned_route2
        "Tell him to leave her alone": 
            jump intervene_route2
        "Help him yourself":
            jump explain_route2
        "Watch from a distance": 
            jump ignore_route2

label intervene_route2:
    pov "Hey! Back off, man. She's busy."
    show man asking at left
    m "What? I was just asking for help. I'm new here."
    show silvie anoyed at right
    s "Im sorry? He was just asking how to use his card. I was helping him."
    pov "Oh."
    pov"My bad. Sorry about that."

    scene bg black
    centered "Jumping to conclusions can create awkward or even hostile situations. It's always best to assess the situation before intervening aggressively."
    jump third_chapter

label ignore_route2: 
    scene bg train
    show man body at left
    show silvie answering at right
    "You decide to hang back for a moment and just watch."
   
    s "See? You just tap it there until it beeps."
    show silvie body at right
    show man asking at left
    m "Thank you so much! You're a lifesaver."

    scene bg black
    centered "Sometimes, observing for a moment is the smartest move. Not all situation are dangerous."
    jump third_chapter

label concerned_route2:
    
    pov "Excuse me, is everything alright here?" 
    show silvie answering
    s "Oh, yeah! I was just showing him how the OV-chipkaart works."
    show silvie body
    show man asking 
    m "This is my first time in the Netherlands. It's a bit confusing!"
    show man body
    pov "Oh, yeah, It get that."
    pov "Well, welcome to the Netherlands! Enjoy your trip."
    show man asking 
    m "Thanks"
    "With a final nod, you turn and get on your bus."

    scene bg black
    centered "Making sure everything is okay without making accusations or jumping to conclusions is a good way to check the situation."
    jump third_chapter

label explain_route2: # needs work? I feel like this one is a bit off
    scene bg train
    show man body at left
    show silvie body at right
    pov "Hey, I can help with that. You just tap your card right on this scanner here."
    show man asking at left
    m "Oh, thanks?"
    show man body at left
    show silvie anoyed at right
    s "I was just explaining that."
    show silvie body at right
    pov "Sorry, just wanted to help."
    pov "Good luck with your trip!" 

    scene bg black
    centered "Offering help is a normal way to subtly enter the situation and gauge the vibe."
    jump third_chapter


label third_chapter:
    scene bg street
    show laura body at right
    show man talking at left

    m "Damn, girl. That dress is something else."
    show man body at left
    l "..." 
    show man talking at left
    m "What, you're too good to say thank you? I'm trying to be nice!" 
    show man body at left
    show laura fuck off
    l "I'm not interested. Go away."
    show laura body flip
    show man talking at left
    m "Fine, whatever. Stuck-up bitch." 
    show man body

    menu:
        "Make fun of him":
            jump sarcastic_intervene_route3
        "Confront him directly":
            jump intervene_route3
        "Ignore it":
            jump ignore_route3

label sarcastic_intervene_route3: 
    pov "Oh wow, thanks for blessing us with your unsolicited opinion. Shall we share it with your mother?" 
    m "What did you just say? Are you asking for a fight?" 

    scene bg black 
    centered "Sarcasm won't get you far. Instead, it will anger the agressor and put both of you and the victim at risk. People are unpredictable, play it safe." 
    jump end_chapter


label intervene_route3:
    pov "Hey, dude. She said she's not interested. Time to go."
    show man whatever
    m "Whatever, man. It's a free country."
    "He glares at you for a second before walking off, muttering under his breath."

    pov "You okay?"
    l "Yeah. Thanks for that. What a creep."
    pov "No problem. Take care."

    scene bg black
    centered "Stepping in and checking up was the right thing to do. That's how you support someone."
    jump end_chapter

label ignore_route3:

    "You walk on, pretending you didn't hear anything."
    
    show laura talking
    l "Don't you call me that!"
    show laura body flip at right
    show man groping
    m "You're asking for it, dressed like that!" 
    "His voice gets louder and more aggressive. He takes a step closer to her."
    
    show laura fuck off 
    l "Get away from me you creep."

    scene bg black
    centered "When harassment escalates, ignoring it can leave the victim in a dangerous situation. Your presence alone could be enough to deter him."
    jump end_chapter


label end_chapter:
    scene bg classroom

    "This is the end of the game. Be sure to try out the different choices and their conequences."
    return