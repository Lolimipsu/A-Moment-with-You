# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Moni = Character("Monika", color ="#5fb629")
define You = Character("[name]", color="#FFF")
#INITIALIZE ARE FOR SPRITES ONLY
init python:
    define.move_transitions("ease", 0.3)

init:
    image HMonika:
        "Monika/o2_3a.png"
        zoom 0.8

init:
    image AMonika:
        "Monika/o2_3b.png"
        zoom 0.8

init:
    image a:
        "Monika/a.png"
        zoom 0.8

init:
    image a1:
        "Monika/a1.png"
        zoom 0.8

init:
    image a2:
        "Monika/a2.png"
        zoom 0.8

init:
    image a3:
        "Monika/a3.png"
        zoom 0.8

init:
    image c:
        "Monika/c.png"
        zoom 0.8

init:
    image idled:
        "Monika/b.png"
        zoom 0.8

init:
    image idle1:
        "Monika/b1.png"
        zoom 0.8

init:
    image g2:
        "g2.png"
        zoom 0.8

init:
    image g3:
        "g3.png"
        zoom 0.8

init:
    image g4:
        "g4.png"
        zoom 0.8

image buggy_monika:
        "g2"
        0.10
        "g3"
        0.10
        "g4"
        0.10
        repeat

image splash ="Logo.png"
image Disclaimer ="Disclaimer.png"
image titles= im.Scale("Title Screen.png", 1280, 720)

#IMAGE SCALED
image school_yard= im.Scale("bg/school_yard.png", 1280, 720)
image park-day= im.Scale("bg/park-day.png", 1280, 720)

image streets = im.Scale("bg/streets-day.png", 1280,720)
image trainstation = im.Scale("bg/trainStation_day.png", 1280,720)
image cafe_in = im.Scale("bg/cafe-inside.png", 1280,720)
image cafe_out = im.Scale("bg/cafe_exterior.png", 1280,720)


#CAFE SCENE MONIKA
image cafeEvent_sm1= im.Scale("cg/m_cg_cafeEvent_1a.png", 1280, 720)
image cafeEvent_sm2= im.Scale("cg/m_cg_cafeEvent_1b.png", 1280, 720)
image cafeEvent_hm1= im.Scale("cg/m_cg_cafeEvent_2a.png", 1280, 720)
image cafeEvent_hm2= im.Scale("cg/m_cg_cafeEvent_2b.png", 1280, 720)
image cafeEvent_vhm1= im.Scale("cg/m_cg_cafeEvent_3a.png", 1280, 720)
image cafeEvent_vhm2= im.Scale("cg/m_cg_cafeEvent_3b.png", 1280, 720)
image cafeEvent_drink= im.Scale("cg/m_cg_cafeEvent_p2.png", 1280, 720)

#Splash Screen
label splashscreen:
    scene black
    with Pause(2)
    play music "audio/The_Early_Bird.ogg"
    show splash with fade
    with Pause(3)
    scene Disclaimer with Dissolve(0.070)
    with Pause(3)
    scene titles with fade
    with Pause(0.010)
    return


# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black
    with dissolve
    stop music fadeout 2

    python:
        name = renpy.input("What is your name?")
        name = name.strip()

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # Dialouge
    pause 2.0
    "Hello? Can You Hear me?"
    "Can you Hear me now?"
    play sound "audio/sfx/s_kill_glitch1.ogg"
    show buggy_monika
    pause 0.5
    "Oh!"
    play music "audio/sfx/interference.ogg"
    "..."
    pause 1.0
    "Ehehe~"
    "This is kinda awkward." # BROKE ASS ENGLISH
    "Hold on, give me a second."
    "Let me try and fix this."
    "How about a little bit of this..."
    pause 1.5
    "And a little bit of that."
    pause 1.5
    "Almost there..."
    hide buggy_monika
    stop music
    play sound "audio/sfx/glitch3.ogg"
    show HMonika
    pause 1.0
    "There we go!"
    "Hi, It's me, Monika."


    play music "audio/Rainclouds_And_Sunshine-Sayoris_Theme.ogg"
    pause 0.5
    scene school_yard
    show HMonika
    with Dissolve(.5)
    pause 0.3
    Moni "Did you miss me?"
    You "Who... are you?"

    hide HMonika
    show AMonika
    with Dissolve(0.2)
    Moni "Hey! That's rude you know!"
    Moni "Don't you miss your cute girlfriend?"
    You "Girlfriend?!"
    You "You?!"
    Moni "Yeah I am your girlfriend silly!"
    Moni "Don't you remember?"
    You "Since when? and how???"
    You "I don't remember having a girlfriend!"


    scene school_yard
    show HMonika
    with Dissolve (0.2)
    Moni "Ahaha~"
    Moni "You're really funny."
    Moni "Anyway, do you want to hang out with me today?"
    You "Well, I..."
    menu:
        "Do you want to spend this day with Monika?"
        "Yes":
            $ answer = "YES"
        "YES":
            $ answer = "YES"
        "No":
            $ answer = "NO"

    if answer == "YES":
        You "Well, sure why not?" # BROKE ASS ENGLISH replaced I don't see

    elif answer == "NO":
        "You refused her offer." # BROKE ASS ENGLISH
        "But for some reason, You can't can't open your mouth and say no to her."
        "Especially with that face."
        "I mean seriously, how could you say no to that face?"
        "Just Monika."
        You "Fine."
    Moni "Yay!"
    hide HMonika
    with easeoutleft
    scene park-day with Dissolve(0.2)
    "Without another word, Monika pulls my hand and dragged me to a nearby park."
    "There we sat for a while and have a little chit-chat." # BROKE ASS ENGLISH
    "Then the awkward silence came." # "that continued for 5 minutes" BROKE ASS ENGLISH
    "I tried to break the silence and brought up where should we be going next."
    You "So...um..."
    show a with Dissolve (0.2)
    pause 1
    "As I turn my head towards her, I saw Monika silently sitting in the bench and watches the people passing by."
    "She looks like having fun."
    "Which makes it more harder now for me to break this awful silence between us."
    "I must break this silence, or we would be sitting here in the park whole day."
    "But sitting here with her and watching people pass by isn't a bad idea at all."
    "But still..."
    You "Hey, Monika."
    hide a
    show a1
    Moni "Hmm...?"
    hide a1
    show a2
    Moni "Oh, Hey [name] what's up?"
    You "What's your plan for today?" #Do you have any plans for today? BROKE ASS ENGLISH
    hide a2
    show idle1
    #BROKE ASS ENGLISH FIX
    Moni "Plans for today?"
    Moni "Hmm..."
    Moni "I don't know." # formerly i dont think so BROKE ASS ENGLISH
    Moni "I didn't thought of it that much."
    Moni "Aside from sitting here in the park watching the people pass by with you."
    Moni "Though my goal was to make you come with me in our little date."#NEEDS FIX, BROKE ASS ENGLISH
    hide idle1
    show idled
    "Damn it, that was unexpected."
    "I thought she planned this very well."
    You "So is there any place do you want go to?"
    You "I mean this Little \date\ of ours will be a waste of time if we only spend it sitting here in the park."
    You "Besides..." #BROKE ASS ENGLISH
    hide idled
    show HMonika
    "As I turn my head towards her and continue to speak, I saw monika with a smug on her face."
    "Oh no."
    Moni"So you are interested in our little date!"
    "!!!"
    You "Well..."
    #Cliche stuff, consider Reworking.
    You "I didn't had a choice, so I must go along."
    You "Besides, I have nothing else better to do anyway."
    You "So having you as company isn't that bad."
    Moni "Hmm~"
    Moni "Fine, fair point."
    hide HMonika
    show a2
    Moni "Though sitting here in the park with you isn't bad idea at all"
    Moni "But ok, so is there a specific place do you want to go to?"
    You "Well..."
    hide a2
    show a1
    menu:
        "Where do you want to go?"
        "Bookstore":
            $ answer = "Shopping"
        "Observation Tower":
            $ answer = "Shopping"
        "Convenience Store":
            $ answer = "Shopping"
        "Movie Cinema":
            $ answer = "Shopping"

    if answer == "Shopping":
        You "Oh I know! why don't we go-"
        hide a1
        show a3
        Moni "Oh I know! Let's go shopping!"
        You "Um, What?"
        You "Can you repeat that again?"
        Moni"Let's go shopping! help me pick cute clothes!"
        "What??"
        "How did it end up like this?"
        You"Well uh..."
        hide a3
        show c
        Moni "You don't want to?"
        "Monika gives you a sad look."
        "That kind of face usually don't work with me." #usually don't work with me BROKE ASS ENGLISH
        "But when it comes to Monika..."
        "It leaves me no choice."
        "I hate this."
        "Why can't I say no to her??"
        You "Fine."
        You "I'll help you pick new clothes."
        hide c
        show a3
        Moni "Yay!"
        hide a3 with Dissolve(0.2)

    ###Walking Scene###
    "After we decided on where should we go next." #CONSIDER FIXING GRAMMAR
    "We stood up and start walking to the train station."
    scene streets with Dissolve(0.2)
    show a with Dissolve (0.2)
    "We took a walk in the nearby neighborhood to get to the train station."
    "On the way there, we see people doing their daily commute, some are having fun, Couples laughing."
    "But, Monika paid most attention on the couples she sees that pass by."
    hide a
    show HMonika
    Moni "Hey [name], aren't they lovely?"
    You "Yeah."
    Moni "Don't they make you feel jealous on how lovey dovey they are?"
    hide HMonika with Dissolve(0.2)
    You "Ye-"
    "Wait NO."
    "That was a close one! I shouldn't doze off!"
    "Looking back at Monika, She's about to burst laughing."
    "She seems to enjoy teasing me this much."
    "But whatever."
    "We continued walking to get to the train station."

    scene cafe_out with Dissolve(0.2)
    "But we got sidetracked when Monika found a nearby cafe"
    "Hey [name]! let's go there! that cafe looks cute!"
    scene cafe_in with Dissolve(0.2)
    "Placeholder - skip to the next scenes"
    
    ###TRAIN SCENE###
    "Though we missed the train when we got there."
    "It seems we'll have to wait until the next train arrives."
    "We both sat at the benches and waited for the next train patiently."

    Moni "Hey [name]"
    You "?"
    Moni "Why did you come along with me?"
    "The Mall isn't that far from here"
    "So there's no need to take a train or a Taxi."
    scene city_day_p with Dissolve(0.2)
    "After some time walking"
    "And some scenery walk"

    ##PICKING CLOTHES
    Moni "So what do you think about this?"
    "The game ends here."
    # This ends the game.
    return
