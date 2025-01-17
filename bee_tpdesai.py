
#################################################
# Term Project
# name: Tresha P Desai
# andrew id: tpdesai
#################################################

from cmu_graphics import *
import math, copy
import decimal
from PIL import Image
import random, time


#################################################
# Citation 
# background: https://www.publicdomainpictures.net/pictures/80000/velka/grass-background-1393979091XaG.jpg
# bee: https://images.search.yahoo.com/search/images?p=bee+images+flapping+gif+no+background&fr=mcafee&type=E211US714G0&imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F02%2Fce%2F79%2F02ce7945c01a4d62f78e480ca9c51f00.gif#id=5&iurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F02%2Fce%2F79%2F02ce7945c01a4d62f78e480ca9c51f00.gif&action=click
# cat: https://images.search.yahoo.com/search/images?p=cat+gif+animated+no+background&fr=mcafee&type=E211US714G0&imgurl=https%3A%2F%2Fwebstockreview.net%2Fimages%2Fclipart-cat-animated-gif-7.gif#id=6&iurl=https%3A%2F%2Fclipground.com%2Fimages%2Fanimated-gif-cat-clipart-5.gif&action=click
#################################################

class Cat():
#################################################
 #cat: https://images.search.yahoo.com/search/images?p=cat+gif+animated+no+background&fr=mcafee&type=E211US714G0&imgurl=https%3A%2F%2Fwebstockreview.net%2Fimages%2Fclipart-cat-animated-gif-7.gif#id=6&iurl=https%3A%2F%2Fclipground.com%2Fimages%2Fanimated-gif-cat-clipart-5.gif&action=click
#################################################    

    def __init__(self,app,x,y,dx=2,dy=4):
        self.x = x 
        self.y = y
        self.dx = dx
        self.dy = dy
        
       
################################################################################
# the code below was taken from Kirby example from Piazza
        
        catGif = Image.open('catgif2.gif')
        self.spriteList1 = []
        self.spriteList2 = []
        for frame in range(catGif.n_frames): 
            
            catGif.seek(frame)
            fr1 = catGif.resize((catGif.size[0]//10, catGif.size[1]//10))
            fr2 = fr1.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            fr1 = CMUImage(fr1)
            self.spriteList1.append(fr1)
            fr2 = CMUImage(fr2)
            self.spriteList2.append(fr2)

        ## fix for broken transparency on frame 0
        self.spriteList1.pop(0)
        self.spriteList2.pop(0)

        # set sprite counters
        self.stepCounter = 0
        self.spriteCounter = 0

    

    def draw(self,app):
        # draw current sprite
        
                
        if app.goRight == True:
            drawImage(self.spriteList1[self.spriteCounter], 
                self.x, self.y, align = 'center')

        elif app.goRight == False:
            drawImage(self.spriteList2[self.spriteCounter], 
                self.x, self.y, align = 'center')
        
        
    def doStep(self,app,wing):
        self.stepCounter += 1
        if self.stepCounter >= wing: 
            self.spriteCounter = (self.spriteCounter + 1) % len(self.spriteList1)
            self.stepCounter = 0

        if self.x < 50 :
            self.x = 50
            self.dx *= -1
            app.goRight = not app.goRight
        elif self.x > 500:
            self.x = 500
            self.dx *= -1
            app.goRight = not app.goRight

        self.x -= self.dx
################################################################################

    def detectCat(self,app,other):
        if isinstance(other,Bee) :
            if distance(app,other.x,other.y,self.x,self.y)< 50:
                app.rotate = True
            else:
                app.rotate = False
        # detect cat function will show red words "OUCH" if app.rotate = True
             
                


        
        


class Bee() :

################################################################################
#bee: https://images.search.yahoo.com/search/images?p=bee+images+flapping+gif+no+background&fr=mcafee&type=E211US714G0&imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F02%2Fce%2F79%2F02ce7945c01a4d62f78e480ca9c51f00.gif#id=5&iurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F02%2Fce%2F79%2F02ce7945c01a4d62f78e480ca9c51f00.gif&action=click
################################################################################
    def __init__(self,app,x,y,dx=0.1,dy=0.1,size=15,pollen = 0):
        self.x = x 
        self.y = y
        self.dx = dx
        self.dy = dy
        
        self.size = size
        self.pollen = pollen

################################################################################
# the code below was taken from Kirby example from Piazza
     
        beeGif = Image.open('beegif.gif')
        self.spriteList1 = []
        self.spriteList2 = []
        for frame in range(beeGif.n_frames): 
            
            beeGif.seek(frame)
            fr1 = beeGif.resize((beeGif.size[0]//5, beeGif.size[1]//5))
            fr2 = fr1.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            fr1 = CMUImage(fr1)
            fr2 = CMUImage(fr2)
            self.spriteList1.append(fr1)
            self.spriteList2.append(fr2)

        # fix for broken transparency on frame 0
        self.spriteList1.pop(0)
        self.spriteList2.pop(0)

        # set sprite counters
        self.stepCounter = 0
        self.spriteCounter = 0

    

    def draw1(self):
        # draw current sprite
        drawImage(self.spriteList1[self.spriteCounter], 
                  self.x, self.y, align = 'center')
    def draw2(self):
        # draw current sprite
        drawImage(self.spriteList2[self.spriteCounter], 
                  self.x, self.y, align = 'center')
        
    def doStep(self,wing):
        self.stepCounter += 1
        if self.stepCounter >= wing: 
            self.spriteCounter = (self.spriteCounter + 1) % len(self.spriteList1)
            self.stepCounter = 0
################################################################################

# to move Player Bee on step

    def movement(self,app):

        if self.x < 0:
            self.x = 5
        if self.y < 0 :
            self.y = 5 
        if self.x > app.width:
            self.x = app.width-5
        if self.y > app.height:
            self.y = app.height -5

        if distance(app,self.x, self.y, app.cx, app.cy) <= 20 :
            self.x = app.cx -9
            self.y = app.cy -9
        else: 
            self.x += self.dx
            self.y += self.dy 
    
        self.dx = (app.cx -self.x)/10

        self.dy = (app.cy-self.y)/10
        
class HelperBee(Bee):

    def __init__(self,app,x,y,dx=0.1,dy=0.1,size=15,pollen = 0):
        super().__init__(app,x,y,dx=0.1,dy=0.1,size=15,pollen = 0)
        self.pollenDict = dict()
    
    # this function is for helper bee to given pollen to flowers     

    def helperGivePollen(self,app, list1):

        # check which flower is nearby

        for flower in list1:
            app.giveOnce = False
            if distance(app,self.x, self.y, flower.x, flower.y) <= 550:
                if flower.x -self.x < 0 :
                    app.goRightBee = True
                elif flower.x - self.x >= 0 :
                    app.goRightBee = False

                # loop through and check if helper bee has correct color pollen in helper inventory
                   
                for pollenId in app.helperBee.pollenDict:
                    if flower.color == self.pollenDict[pollenId] and app.giveOnce == False and flower.pol == 0 :
                        app.giveOnce = True
                          
                        # if one pollen is used, app.giveOnce is True so that we keep remaining pollens in inventory
                        # this means that each flower can only be pollinated with one pollen

                        self.dx = (flower.x -self.x)/90
                        self.dy = (flower.y-self.y)/90
                        self.x += self.dx
                        self.y += self.dy
                        
                        # once the distance of helper bee is close enough to flower, we will pollinate the flower

                        if distance(app,self.x, self.y, flower.x, flower.y) <= 40:
                            
                            HelperBee.movement(self,app,flower)
                            self.dx = (flower.x -self.x)
                            self.dy = (flower.y-self.y)

                            self.x = flower.x
                            self.y = flower.y
                          
                            flower.pol = 1 
                            # for flower to just grow
                            app.idList.append(flower.id) 
                            
                      
         
    # this is similar to the one above with some parameters changed so that the bees have slight difference in functionality

    def helperGivePollen2(self,app, list1):
        for flower in list1:
            app.giveOnce = False
            if distance(app,self.x, self.y, flower.x, flower.y) <= 400:
                if flower.x - self.x < 0 :
                    app.goRightBee = True
                elif flower.x - self.x >= 0 :
                    app.goRightBee = False
                    
                for pollenId in self.pollenDict:
                    if flower.color == self.pollenDict[pollenId] and app.giveOnce == False and flower.pol == 0 :
                        app.giveOnce = True
                          
                        self.dx = (flower.x -self.x)/90
                        self.dy = (flower.y-self.y)/90
                        self.x += self.dx
                        self.y += self.dy
                            
                        if distance(app,self.x, self.y, flower.x, flower.y) <= 40:
                            
                            HelperBee.movement(self,app,flower)
                           
                            self.x = flower.x
                            self.y = flower.y
                            self.dx = (flower.x -self.x)
                            self.dy = (flower.y-self.y)
                            flower.pol = 1 
                            # for flower to just grow
                            app.idList.append(flower.id) 
                            
                       
           
    # helper bee to take pollen 

    def helperTakePollen(self,app, list1):
        
      

        # run through a loop and check if pollen nearby

        for pollen in list1:
            

            if distance(app,self.x, self.y, pollen.x, pollen.y) <= 300:

                self.dx = (pollen.x -self.x)/90
                self.dy = (pollen.y-self.y)/90
                self.x += self.dx
                self.y += self.dy
            
            
                if distance(app,self.x, self.y, pollen.x, pollen.y) <= 50 and pollen.pol == 1 and len(self.pollenDict)<6:

                    HelperBee.movement(self,app,pollen)
                    self.x += self.dx
                    self.y += self.dy

                    self.dx = (pollen.x -self.x)
                    self.dy = (pollen.y-self.y)
                    
                    if pollen.x -self.x < 0 :
                        app.goRightBee = True
                    elif pollen.x - self.x >= 0 :
                        app.goRightBee = False
                    self.x = pollen.x
                    self.y = pollen.y
                    self.pollenDict[pollen.id] = pollen.color
                    pollen.pol = 0
                    pollen.ring = True
                   
                
            else:
                
                self.x += self.dx 
                self.y += self.dy 
              
    # this code is similar but with some modifications to second helper bee
    #            
    def helperTakePollen2(self,app, list1):
   

        for pollen in list1:

            if distance(app,self.x, self.y, pollen.x, pollen.y) <= 500:

                self.dx = (pollen.x -self.x)/90
                self.dy = (pollen.y-self.y)/90
                self.x += self.dx
                self.y += self.dy
                HelperBee.movement(self,app, pollen)
            
                if distance(app,self.x, self.y, pollen.x, pollen.y) <= 50 and pollen.pol == 1 and len(self.pollenDict)<6:

                    self.dx = (pollen.x -self.x)/90
                    self.dy = (pollen.y-self.y)/90
                    self.x += self.dx
                    self.y += self.dy


                    
                    if pollen.x -self.x < 0 :
                        app.goRightBee = True
                    elif pollen.x - self.x >= 0 :
                        app.goRightBee = False
                    self.y += self.dy
                    self.x += self.dx
                    self.x = pollen.x
                    self.y = pollen.y
                    self.pollenDict[pollen.id] = pollen.color
                    pollen.pol = 0
                    pollen.ring = True
                    self.dx = (pollen.x -self.x)
                    self.dy = (pollen.y-self.y)
                   
                
                    
            else:
                
                self.x += self.dx 
                self.y += self.dy 
               
               
    # for helper bee to move onStep

    def movement(self,app,other):

        if self.x < 0:
            self.x = 5
        if self.y < 0 :
            self.y = 5 
        if self.x > app.width:
            self.x = app.width-5
        if self.y > app.height:
            self.y = app.height -5
               
            
            self.x += self.dx
            self.y += self.dy 
        
        self.dx = (other.x -self.x)/10
        self.dy = (other.y-self.y)/10 
   
# pollen score on top left screen is called inventory 
# there will be 3 inventories in all, one for each bee

class Inventory():


    def __init__(self,app,colorList = [], dict1=dict()):
     
        
        self.colorList = colorList
        self.dict1 = dict1

    def addColor(self,app,color):

        self.colorList.append(color)
      



class Pollen():

    def __init__(self,app,x,y,color,id,dx=0,dy=0,speed=5,size=8, pol=1, ring = False):
        self.x = x 
        self.y = y
        self.dx = dx
        self.dy = dy
        self.speed = speed
        self.size = size
        self.pol = 1
        self.color = color
        self.id = id
        self.ring = ring

    def pollenMove(self):
        self.y += 1
        self.x += math.sin(100*self.y+ 400)

    def pollen(self):

        self.pol = 0

@staticmethod

class Flower():
    
    

    def __init__(self,app,x,y,color,id,dx=0,dy=0,speed=5,size=8, pol=0, pollenGrow = False):
        self.x = x 
        self.y = y
        self.color = color
        self.dx = dx
        self.dy = dy
        self.speed = speed
        self.size = size
        self.pol = pol
        self.id = id
        self.pollenGrow = False
        


    def flowerMove(self):
        self.y += 1
        self.x += math.sin(100*self.y+ 400)

    def pollenAdded(self):
        self.pol = 1
    


#################################################
# Helper Functions

#################################################

# to move flowers down the screen 

def moveBlueFlower(app, list1,idList1):
    
    for flowerB in list1:
        flowerB.flowerMove()
        
        if flowerB.y > app.height:
            id = flowerB.id
            list1.remove(flowerB)
            if id in idList1:
                idList1.remove(id)
            
            x = random.randrange(app.width)
            colorList = ['red','blue','yellow','green']
            color = colorList[random.randrange(4)]
            flower = Flower(app,x,0,color,id)
            list1.append(flower)
            





# to move pollen down the screen

def movePollen(app,list1, idList1, idDict1):
    for pollen1 in list1:
        pollen1.pollenMove()
        if pollen1.y > app.height:
            id = pollen1.id
            list1.remove(pollen1)
            if id in idList1:
                idList1.remove(id)
                if id in idDict1:
                    del idDict1[id]
            
            x = random.randrange(app.width)
            colorList = ['red','blue','yellow','green']
            color = colorList[random.randrange(4)]
            pollen1 = Pollen(app, x, 0,color,id)
            pollen1.pol = 1
            list1.append(pollen1)

# check if bee near any flower and remove its pollen

def beeNearRemoveBluePollen(app,list1):
    for pollen1 in list1:
        if distance(app,pollen1.x, pollen1.y, app.bee.x, app.bee.y)< 25:
            
            if app.flowerCountBlue < 6 and pollen1.pol != 0:
                

                
                
                app.flowerCountBlue += 1   
                
                app.inventoryList.append(pollen1.color)
                app.inventoryDict[pollen1.id] = pollen1.color
                app.idListPollen.append(pollen1.id)
                pollen1.pollen()
                
                pollen1.ring = True

            elif app.flowerCountBlue >= 6 and pollen1.pol != 0:

                app.inventoryList.pop(0)
                key1 = app.idListPollen.pop(0) 
                del inventoryDict[key1]
                app.inventoryList.append(pollen1.color)
                app.inventoryDict[pollen1.id] = pollen1.color
                pollen1.pollen()
              
                pollen1.ring = True
                




# if bee any flower, pollinate it if there are pollens in inventory

def beeNearAddBluePollen(app, list1):
 
    
    for flowerTP in list1:
       
        if distance(app,flowerTP.x, flowerTP.y, app.bee.x, app.bee.y)< 50:
            
            if flowerTP.color in app.inventoryList and flowerTP.pol != 1:
    
                app.finalScore += 10
                app.idList.append(flowerTP.id)  
                # to grow flowers gradually
                flowerTP.pol = 1
                
                for key in app.inventoryDict :
                    app.oneAdded = False
                    if app.inventoryDict[key] == flowerTP.color and flowerTP.pollenGrow == False and app.oneAdded == False:
                        
                        app.pollenGrowList.append(key)
                        oneAdded = True
                        flowerTP.pollenGrow = True

                app.inventoryList.remove(flowerTP.color) 
              
                app.flowerCountBlue -= 1 
                
# to loops through pollen id and check if pollen still on screen then it will grow
# to loop through flower id and if it is pollinated and is on screen it will grow

def idList(app,idList, flowerList, pollensList, pollenGrowList):
    for flower in flowerList:
        for id1 in idList:
            if flower.id == id1 and flower.pol ==1 :
                if app.timerValue % 10 == 0 :
                    flower.size += 1 

                if flower.size > 25 :
                    flower.size = 25
                    app.collision = False
                elif flower.size < 16 :
                    app.collision = True

    for pollen in pollensList:
        for id2 in pollenGrowList:
            if pollen.id == id2 and pollen.pol == 0:
                if app.timerValue % 10 == 0 :
                    pollen.size += 1
                if pollen.size > 25:
                    pollen.size = 25

    
    

    
# draw the multicolored flowers and pollens

def drawBlueFlowers(app,list1):

    for i in range(len(list1)):

       
            
        drawCircle(list1[i].x, list1[i].y, list1[i].size, fill = list1[i].color, border = "black")
     
        drawRegularPolygon(list1[i].x, list1[i].y, list1[i].size+10, 6, fill=None, border='black',
                       rotateAngle=app.angle)
       
def drawBluePollen(app,list1):
    for i in range(len(list1)):
        
        if list1[i].ring == True:
            
            drawCircle(list1[i].x, list1[i].y, list1[i].size, fill = None, border = list1[i].color, borderWidth = 5)
        else:
            drawCircle(list1[i].x, list1[i].y, list1[i].size, fill = list1[i].color, border = list1[i].color, borderWidth = 5)


# create a list of flowers

def createFlowers(app,colorList):
    flowerList = list()
    id = 0
    for f in range(16):
        
        x = random.randrange(app.width)
        y = random.randrange(app.height)
        flower = Flower(app,x,y,colorList[f%4], id)
        id += 1
        
       
        flowerList.append(flower)
    return flowerList

# create a list of pollens

def createPollen(app, colorList):
    pollenList = list()
    id = 0
    for f in range(10):
        x = random.randrange(app.width)
        y = random.randrange(app.height)
        pollen = Pollen(app,x,y,colorList[f%4],id)
        id += 1
        
        
       
        pollenList.append(pollen)
    return pollenList

# calculate distance function

def distance(app, x1,y1,x2,y2):

    distance = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    return distance





#################################################
# Test animation 
#################################################
def onAppStart(app):
    resetApp(app)
def resetApp(app):

    
   
    # player bee location and cat location 
    app.bx = 5
    app.by = 5
    app.catx = 550
    app.caty = 550
    # helper bee location
    app.helperBeex =  10 
    app.helperBeey = 10
    app.helperBee2x = 300
    app.helperBee2y = 300 
    # cursor location 
    app.cx = -500
    app.cy = -500
    # create bee and helper bee instances
    app.bee = Bee(app, app.bx,app.by)
    app.helperBee = HelperBee(app, app.helperBeex,app.helperBeey)
    app.helperBee2 = HelperBee(app, app.helperBee2x,app.helperBee2y)
    app.cat = Cat(app,app.catx,app.caty)
    # background image
    # background: https://www.publicdomainpictures.net/pictures/80000/velka/grass-background-1393979091XaG.jpg
    app.imagebg = Image.open("background.jpg")
    app.imagebg = CMUImage(app.imagebg)
    # pollen count to make sure pollen inventory does not exceed 6
    app.flowerCountBlue = 0
    # final score for each flower pollinated, give it 10 points
    app.finalScore = 0
    # flower angle for rotation per timestep
    app.angle = 5
    # store colours in pollen inventory
    # pollen color touched by bee added to inventory
    # there is an inventory list and inventory dictionary
    app.inventory = Inventory(app,colorList=[],dict1 = dict())
    app.inventoryList = app.inventory.colorList
    app.inventoryDict = app.inventory.dict1
    # id list if for the flower id. Not required but easier to tell if the flower is pollinated, its id goes in this list 
    # all flower ids in this list will grow if the flower is still on screen
    app.idList = []
    # random pollen color generated, red, blue, yellow and green
    app.pollenList = ["red","blue","yellow","green"]
    # pollen id list, if pollen taken, the pollen id goes in this list
    # pollen inventory dictionary to check if the pollen is still on screen
    app.idListPollen = []
    # create flowers and create pollen on start
    app.flowerListBlue = createFlowers(app, app.pollenList)
    app.pollensList = createPollen(app, app.pollenList) 
    # timer for allowing pollen and flower to grow gradually
    app.timerValue = 0 
    # if pollen that was taken was used to pollinated a flower, then its id is added to this list to grow
    # we will loop through the id to check if the pollen is still on screen and it will grow if it is
    app.pollenGrowList= []
    # a checkpoint to make sure that if there are several pollens of same color in inventory\
    # when it loops through the inventory Dict, we only one to utilise one color and not all of the same color
    # once we found one color, we add that pollen id to grow list and switch this boolean from False to True
    app.oneAdded = False
    app.oneAddedHelper = False
    # helper bee to only give pollen to one flower and not multiple times 
    app.giveOnce = False 
    # for collision of flowers
    app.collision = False
    # wing speed for player bee
    app.wing = 1000

    # for pause key
    app.paused = False
    # meow cat if Player bee nearby
    app.rotate = False
    app.goRight = False
    # for helperbee direction facing
    app.goRightBee = False
    # for sprite movements for helper bees
    app.helperValue = 10
    app.helperValue2 = 10
   



 

def onMouseMove(app, mouseX, mouseY):
   app.cx = mouseX
   app.cy = mouseY
 
def onStep(app):
    
    takeStep(app)

def takeStep(app):
    if not app.paused:
       
        # flower angle of rotation per step # just an extra visual feature
        # time value for growth rate of flower or pollen
        value = distance(app,app.bee.x, app.bee.y, app.cx, app.cy)
        #app.valueHelper = (app.helperBee.x)*(app.helperBee.y)*(app.helperBee.x)*(app.helperBee.y)
        #app.valueHelper2 = (app.helperBee2.x)*(app.helperBee2.y)*(app.helperBee2.x)*(app.helperBee2.y)
        app.bee.doStep(app.wing/(6*value))
        app.helperValue = math.sqrt((app.helperBee.dx)**2 + (app.helperBee.dy)**2)
        app.helperValue2 = math.sqrt((app.helperBee2.dx)**2 + (app.helperBee2.dy)**2)
        app.helperBee.doStep(app.wing/app.helperValue**7)
        app.helperBee2.doStep(app.wing/app.helperValue2**7)
        app.angle +=5 
        app.timerValue += 1
        app.cat.doStep(app,10)
       
    
        # move flower down screen over time step

        moveBlueFlower(app, app.flowerListBlue, app.idList)
    
        # move pollen down screen over time step

        movePollen(app,app.pollensList,app.idListPollen, app.inventoryDict)
        
        # bee moves near cursor speeding up if cursor is further away
        # also, bee should not fly out of canvas
    
        app.bee.movement(app)

        # both helper bees taking pollen 
        app.helperBee.helperTakePollen(app, app.pollensList)
        app.helperBee.helperGivePollen(app, app.flowerListBlue)
        

        # if bee is near blue flowers, the pollen is removed and blue flower turns white
        
        beeNearRemoveBluePollen(app,app.pollensList)
        
        
        # if bee near light blue flower, pollinate it, flower grows in size
        # blue pollen score count decreases by 1
        # add 10 points to final score

        beeNearAddBluePollen(app, app.flowerListBlue)

        # for pollen to grow if the flower is pollinated by that pollen
        # for flower to grow once pollinated

        idList(app,app.idList, app.flowerListBlue, app.pollensList, app.pollenGrowList)
        
        # both helper bees giving pollen to flowers
        

        #collision(app,app.flowerListBlue)

        app.helperBee2.helperTakePollen2(app, app.pollensList)
        app.helperBee2.helperGivePollen2(app, app.flowerListBlue)

        # if player bee near cat, it will meow

        app.cat.detectCat(app,app.bee)
        
        


def onKeyPress(app,key):
    if key == "p":
        app.paused = not app.paused
    if key == "r":
        resetApp(app)

def redrawAll(app):


   # draw background grass image

    drawImage(app.imagebg, 0,0)
    

    # draw blue flowers

    drawBlueFlowers(app,app.flowerListBlue)
    
    # draw light blue flowers

    drawBluePollen(app,app.pollensList)
    
    # draw Circle for the cursor
    drawCircle(app.cx,app.cy,3, fill="blue", border="black") # cursor

    # draw yellow circle for the player bee and overlap it with beegif

    drawOval(app.bee.x,app.bee.y,20,12, fill="yellow", border="black") # bee
    if app.cx -app.bee.x >= 0:
        app.bee.draw1()

    else:
        app.bee.draw2()
    # draw helper bee 1

    drawOval(app.helperBee.x,app.helperBee.y,20,12, fill="purple", border="black") 
    if app.goRightBee==True :
        app.helperBee.draw1()

    else:
        app.helperBee.draw2()
    # draw helper bee 2

    drawOval(app.helperBee2.x,app.helperBee2.y,20,12, fill="pink", border="black")
    if app.goRightBee==True :
        app.helperBee2.draw1()

    else:
        app.helperBee2.draw2()
        
    # draw cat
    
    app.cat.draw(app)
 
    # draw pollen inventory list at top left hand corner
    x = 10
    y = 20
    f1 = 1
    for c in app.inventoryList:
        drawCircle(x,y,10,fill = None, border = c, borderWidth = 5)
        drawCircle(app.bee.x-10+f1, app.bee.y+30,5, fill = None, border = c, borderWidth=5 )
        x += 12
        f1 += 5
    
    # draw pollen inventory list at top left hand corner for helper bee
    f2 = 1
    xh = 10
    yh = 45
    for key in app.helperBee.pollenDict:
        drawCircle(xh,yh,10,fill = app.helperBee.pollenDict[key], border = "purple", borderWidth = 3)
        drawCircle(app.helperBee.x-10+f1, app.helperBee.y+30,5, fill = None,border=app.helperBee.pollenDict[key], borderWidth=5 )
        xh += 12
        f2 += 5


    # draw pollen inventory list at top left hand corner for helper bee 2
    f3 = 1
    xh2 = 10
    yh2 = 65
    for key in app.helperBee2.pollenDict:
        drawCircle(xh2,yh2,10,fill = app.helperBee2.pollenDict[key], border = "pink", borderWidth = 3)
        drawCircle(app.helperBee2.x-10+f3, app.helperBee2.y+30,5, fill = None,border=app.helperBee2.pollenDict[key], borderWidth=5 )
        xh2 += 12
        f3 += 5


    # label final score label at top right-hand-corner
    # label pollen count at top right-hand-corner
    
    drawLabel(f'The final score is: {app.finalScore}.', 550,70, font = "arial", size = 15, bold = True)    
    drawLabel(f'The pollen count is: {app.flowerCountBlue}.', 550,90, font = "arial", size = 15, bold = True)
    drawLabel(f'Move the cursor and touch pollen to pollinate flowers.', 350,15, font = "arial", size = 15, bold = True)
    drawLabel(f'Press "r" ro RESET or "p" to PAUSE! ', 350,35, font = "arial", size = 15, bold = True)
    
    if app.rotate:
        drawLabel("Meowww! OUCH!!!", 320,350, font = "arial", size = 30, bold=True, fill="red")
    # draw collision
    if app.collision == True :
        drawLabel(f'Flower Pollinated!Awesome!',320,250,font="arial", bold=True, size= 16)

    # app paused label

    if app.paused:
        drawLabel(f'You have paused the game', 320,200,font="arial", size = 35)
   

#################################################
# main
#################################################

def main():
    
    runApp(width=650, height=650)

if __name__ == '__main__':
    main()