add_library("sound")


    
# import random 

def setup():
    global sf
    global twovtwo
    global page
    global yogoogle, x, y, gameStarted, firstScreen, onevone, twovtwo, presshere, score
    global gameStarted
    global gameclock
    global startTimer
    global currentTime
    size(1680, 1000)
    background(90, 100, 255)
    yogoogle = "YO GOOGLE"
    img = loadImage("multipleandroids.jpg")
    image(img, 0, 0, 1680, 1000)
    
    sf = SoundFile(this, "ransom.mp3")
    playMusic()
    
    x = True
    y = True
    x2 = True
    y2 = True
    firstScreen(x, y)
    # secondScreen (x2,y2)
    gameStarted = False
    # frameRate = 10
    playerone = False
    playertwo = False
    presshere = "Press Here"
    page = 1
    score = 0
    currentTime = millis()
    startTimer = 0
    
    # Throwback = {"PYT":minim.loadFile("PYT.mp3"), 
    #                 "If it isn't Love":minim.loadFile("If it Isn't Love.mp3"), 
    #                 "MyPrerogative":minim.loadFile("MyPrerogative.mp3"),
    #                 "Pretty brown eyes":minim.loadFile("Pretty brown eyes.mp3")}
    
    # R&B = {"We Belong Together":minim.loadFile("We Belong Together.mp3"), 
    #             "My Boo":minim.loadFile("My Boo.mp3"), 
    #             "Shawty like mine":minimloadFile("Shawty like mine.mp3"),
    #              "No One":minim.loadFile("No One.mp3")}
    
    # HipHop = {"In da Club":minim.loadFile("In Da Club.mp3"), 
    #                "Mr.Carter":minim.loadFile("Mr.Carter.mp3"),
    #                 "Pretty Boy Swag":minimloadFile("Pretty Boy Swag.mp3"),
    #                "Gold Digger":minim.loadFile("Gold Digger.mp3")}
    
    # R&B = {"Love Galore":minim.loadFile("Love Galore.mp3"), 
    #            "Shot clock":minim.loadFile("Shot clock.mp3")}
    
    # HipHop = {"Old Town Road":minum.loadFile("Old Town Road.mp3"), 
    #               "Money in the grave":minim.loadFile("Money in the gave.mp3")}
    
    # Pop = {"Baby One more Time":minim.loadFile("Baby One more Time.mp3"), 
    #        "I Got a Feeling":minim.loadFile("I Got a Feeling"),
    #        "Baby":minim.loadFile("Baby.mp3"), 
    #        "Sugar":minim.loadFile("Sugar.mp3")}
           
    # minim=Minim(this)

    
 
def firstScreen(x, y):
# start screen
    fill(random(255), random(255), random(255))
    textSize(90)
    text("YO GOOGLE", 800, 1200)
    text(yogoogle, 570, 100)
    textSize(42)
    fill(0)
    text("Click To Begin YO GAME", 600, 900)
# second screen
def draw():
    pass
    global gameActive
    global gameclock
    global gameStarted
    global gameclock
    global startTimer
    global currentTime
    
    # currentTime = millis()
    # if gameStarted == True:
    #     gameclock = (currentTime - startTimer) / 1000
    #     fill(52, 67, 235)
    #     noStroke()
    #     rect(100, 500, 60, 40)
    #     f = createFont("Roboto-BlackItalic.ttf", 40)
    #     textFont(f)
    #     fill(0)
    #     noStroke()
    #     text(gameclock, 100, 500)
    #     if gameclock == 15:
    #         gameStarted = False
             

def mousePressed():
    global page
    if mousePressed:
        secondScreen()
    if page == 1:
        if mouseX > 300 and mouseX < 550 and mouseY > 300 and mouseY < 550:
            onevone()
            page == 2
        elif mouseX > 1000 and mouseX < 1350 and mouseY > 250 and mouseY < 500:
            twovtwo()
            page == 3
        else:
            print("done")
    # elif page == 4:
    #     if mouseX >= rectangle_width and mouseY >= rectangle_height:
    #         rect(mouseX, mouseY, 1025, 350)
    #         twovtwo()
    #         page = page + 1

    global gameStarted
    gameStarted = True


def secondScreen():

    print("To Do")
    size(1680, 1000)
    background(0, 110, 255)
    img = loadImage("android.jpg")
    image(img, 0, 0, 250, 150)
    image(img, 1450, 0, 250, 150)
    fill(random(255), random(255), random(255))
    textSize(90)
    text("YO GOOGLE", 800, 1200)
    text(yogoogle, 570, 100)

# rect 1

    fill(0)
    if mousePressed:
        rect(300, 250, 350, 250)
        fill(255)
        textSize(90)
        text("1 v 1", 320, 350)
    # text(onevone ,320,350)
        textSize(32)
        text("Press Here", 325, 450)

# rect 3
    fill(0)
    if mousePressed:
        rect(1000, 250, 350, 250)
        fill(255)
        textSize(90)
        text("2 v 2", 1025, 350)
        textSize(32)
        text("Press Here", 1020, 450)
        text(presshere, 1020, 450)

def onevone():
    print("done")
    background(52, 67, 235)
    img = loadImage("android_logo.png")
    image(img, 0, 200, 450, 450)
    img = loadImage("android2.png")
    image(img, 1250, 225, 450, 450)
    fill(255)
    textSize(40)
    text("Yo Score: ", 0, 100)
    text(score, 185, 100)
    fill(0)
    textSize(40)
    text("Yo Score: ", 1400, 100)
    text(score, 1600, 100)
    fill(random(255), random(255), random(255))
    textSize(90)
    text("YO GOOGLE", 800, 1200)
    text(yogoogle, 570, 100)
    
#Songs Randomized from each category
def playMusic():
    global sf
    

    print("peaches")
def draw():
    global score
    if keyPressed and key == 't' or key == 'T':
        sf.play()
    if keyPressed and key == 's' or key == 'S':
        sf.stop()
    if keyPressed and key == 'q' or key == 'Q':
        score += 100
    else:
        print("not right")
        
    if keyPressed and key == 'W' or key == 'w':
        score += 100
    else:
        print("not right")
        
    if keyPressed and key == 'E' or key == 'e':
        print("stop")
        score += 100
    
    
    


# Gameclock
def twovtwo():
    pass
    textSize(80)
    fill(255,0,0)
    text("Round1",1000,100)
    
    
    
        
#     global gameStarted
#     global gameclock
#     global startTimer
#     global currentTime

    # currentTime = millis()
    # if gameStarted:
    #     gameclock = (currentTime - startTimer)/1000
    #     fill(240,244,247)
    #     noStroke()
    #     rect(1100,0,60,40)
    #     f = createFont("Roboto-BlackItalic.ttf",20)
    #     textFont(f)
    #     fill(0,0,0)
    #     text(gameclock, 1100,500)
    #     seconds = 60
        

    size(1680, 1000)
    background(52, 67, 235)

    f = createFont("Roboto-BlackItalic.ttf", 40)
    textFont(f)
    fill(0, 0, 0)
    text("Time:", 0, 500)
    
