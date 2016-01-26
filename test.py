from music import *
from java.awt import Font
from gui import *
from image import *
from timer import *

#from osc import *

## DEFINE DISPLAYS
d = Display("PAGE 1", 900, 600)
d1 = Display("PAGE 2", 900, 600)
d1.hide()

logo = Icon("logo.png")

#oscIn = OscIn(57110) #receiveing messages from port 57110

#
#def simple(message):
#    print "hello world"
#
#def complete(message):
#    OSCaddress = message.getAddress()
#    args = message.getArguments()
#    
#    #print osc message time and address
#    print "\nOSC Event:"
#    print "OSC In - Address:", OSCaddress,
#    for i in range(len (args)):
#            print ", Argument ", + str(i) + ";" + str(args[i]),    
#    print
#
#oscIn.onInput("/helloWorld", simple)
#
#oscIn.onInput("/.*", complete)


##UPLOAD FILE FUNCTION
def uploadfile():
    d.hide()
    d1.show()
    
##BUTTON FUNCTION
def playpause():
  #function goes here
  triangle.stop;
    
    
##DEFINE VARIABLES

lyrics1 = "THIS IS THE GRID"
##-----UPLOAD BTN
button1 = Button("Upload File", uploadfile)
##-----UPLOAD BTN
button2 = Button("Play/pause", playpause)

##----OUTER GRID
## x = (100,100)
## y = (500, 400)
## width 300
## height


#---------- OUTER SQUARE-----------------------------------
bigWidth = 400;
bigRec = Rectangle(100, 100, 500, 400, Color.WHITE,0, 3)

d1.add(bigRec)


#---------- INNER GRID-----------------------------------

## ---- initialize variables
recSize = 25
start = 100
end = start + recSize
length = bigWidth/recSize 
i = 0

#draw rec1
rec = Rectangle(start,start, end, end, Color.WHITE,0, 3)
d1.add(rec)

#----------DRAW INNER GRID-----------------------------------

#for i in range(0, length):
#    start1 = start + (recSize * i)
#    end1 = start1 + (recSize * i) 
#    rec1 = Rectangle(start,start1, end, end1, Color.BLUE,0, 3)
#    i += i
#    ##if i%10 == 0:
#    for j in range (0, i ):
#        start2 = start + (recSize * j)
#        end2 = start1 + (recSize * j)
#        rec2 = Rectangle(start1,start2, end1, end2, Color.RED,0, 3)
#        d1.add(rec2)
#        j+=j

    
   ## d1.add(rec1)
    



##-------------PLAYHEAD-----------------------------------
playhead = Polygon([ 100, 100, 125], [ 400, 450, 425], Color.WHITE)
d1.add(playhead)
value = 10
for i in range (0,10):
    playhead = Polygon([ 100 + value, 100 + value, 125 + value], [ 400, 450, 425], Color.WHITE)
    d1.add(playhead)
    value = value + 10
    i = i + 1
def runPlay():
    i = 0
    value = 10
    for i in range (0,10):
        playhead = Polygon([ 100 + value, 100 + value, 125 + value], [ 400, 450, 425], Color.WHITE)
        d1.add(playhead)
        value = value + 10
        i = i + 1
    t.stop()
    
t = Timer(3000, runPlay, value , True)
   
t.start()


##-------------GENRES--------------------------------------
def itemSelected(itemSelected):
    #function goes here
    string = itemSelected
ddl1 = DropDownList(["nature", "rock", "hip hop"], itemSelected)

soundText = "SOUNDS: "
label2 = Label(soundText)
label2.setFont(Font("Sans", Font.BOLD, 20))
label2.setForeground(Color.WHITE);


d1.add(ddl1, 750, 150)
d1.add(label2, 600, 150)

def saveImage():
    ##save image here
    save = "saved"
    
button3 = Button("save", saveImage)
saveText = "SAVE:   "
label2 = Label(saveText)
label2.setFont(Font("Sans", Font.BOLD, 20))
label2.setForeground(Color.WHITE);


d1.add(button3, 750, 350)
d1.add(label2, 600, 350)
#textarea = TextArea("WELCOME TO PICSEL", 5, 100)
#textarea.setFont(Font("Georgia", Font.PLAIN, 14))

##-----GRID 2 HEADER
label1 = Label(lyrics1)
label1.setFont(Font("Serif", Font.BOLD, 28))
label1.setForeground(Color.GRAY);

##---SET DISPLAY COLORS
d.setColor( Color(0, 0, 0) );
d1.setColor( Color(0, 0, 0) );


##----SET DISPLAY ELEMENTS
d.add(button1, 400, 360);
d.add(logo, 150, 150);
d1.add(label1, 200, 50);
