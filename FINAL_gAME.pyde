def setup():
    global page
    global yogoogle,x,y,gameStarted,firstScreen,onevone,twovtwo,presshere,score
    size(1680,1000)
    background(90, 100, 255)
    yogoogle = "YO GOOGLE"
    img = loadImage("multipleandroids.jpg")
    image(img,0,0,1680,1000)
    x = True
    y = True
    x2 = True
    y2 = True
    firstScreen(x,y)
    # secondScreen (x2,y2)
    gameStarted = False
    # frameRate = 10
    playerone = False
    playertwo = False
    presshere = "Press Here"
    page = 1
    score = 0
    

    
    
    
def firstScreen(x,y):
# start screen
    fill(random(255),random(255),random(255))
    textSize (90)
    text ("YO GOOGLE", 800,1200)
    text(yogoogle ,570,100)
    textSize(42)
    fill(0)
    text ("Click To Begin YO GAME", 600, 900)
#second screen
def draw():
    pass
def mousePressed():
    global page
    if page == 1:
         secondScreen()
         page = page + 1
    elif page == 2:
        onevone()
        page = page + 1
    global gameStarted
    gameStarted = True
   
    
    
            
def secondScreen():
    # print("To Do")
    size(1680,1000)
    background(0,110,255)
    img = loadImage("android.jpg")
    image(img,0,0,250,150)
    image(img,1450,0,250,150)
    fill(random(255),random(255),random(255))
    textSize (90)
    text ("YO GOOGLE", 800,1200)
    text(yogoogle ,570,100)
#rect 1 
    fill(0)
    rect(300,250,350,250)
    fill(255)
    textSize (90)
    text ("1 v 1", 320,350)
    # text(onevone ,320,350)
    textSize(32)
    text ("Press Here", 325,450)
# rect 3 
    fill(0)
    rect(1000,250,350,250)
    fill(255)
    textSize (90)
    text ("2 v 2", 1025,350)
    textSize(32)
    text ("Press Here", 1020,450)
    text(presshere,1020,450)
    

        

def onevone():
    print("done")
    background (52, 67, 235)
    img = loadImage ("android_logo.png")
    image(img,0,200,450,450)
    img = loadImage ("android2.png")
    image(img,1250,225,450,450)
    fill (255,0,0)
    textSize(90)
    text("YO SCORE: ",0,100)
    text(score,500,100)
    fill(0)
    text("YO SCORE: ",1100,100)
    text(score,1575,100)
    
