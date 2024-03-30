from turtle import *
from random import randint
# vérificaction des modules importés
try:
    from PIL import Image
    pillow_installed = True
except:
    print("Oops! - ModuleNotFoundError: No module named 'PIL' - RTFM :")
    print("https://nsi.xyz/py2png")
    pillow_installed = False
titre = "Perspective - Un paysage Synthwave"
title(titre+" | Au lycée, la meilleure spécialité, c'est la spé NSI")
setup(1280, 720) # définit la taille de la fenêtre
colormode(255) # permet l'utilisation de couleurs rgb
tracer(2) #Remplaçable par tracer(2) (10x plus rapide) mais si il est utilisé des lignes du pavage peuvent manquer
hideturtle() #dissimule la tortue

def fond():
    penup()
    rciel = 0
    gciel = 0 
    bciel = 0
    hauteur = -360
    goto(-642,-358)
    pendown()
    while hauteur != 360:
        pencolor(round(239 + rciel), round(41 + gciel), round(209 + bciel))
        forward(1280)
        hauteur += 1
        goto(-640, hauteur)
        rciel += (-29/180)
        gciel += (2/45)
        bciel += (7/720)
        
def etoile():
    for i in range(90):
        penup()
        goto(randint(-720,720), randint(0,360))
        pendown()
        pencolor(255, 255, 255)
        lcercle = randint(1,3)
        fillcolor('white')
        begin_fill()
        circle(lcercle)
        end_fill()
        
def soleil():
    penup()
    liste1 = [10,7,5,4,3,3,3,3,2,2,2,2,2,2,2,1,2,1,2,1,1,2,1,1,1,1,2,1,1,1]
    liste2 = [1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
    pliste1 = 0
    pliste2 = 0
    rsoleil = 0
    gsoleil = 0
    bsoleil = 0
    lsoleil = 8
    hauteur = 30
    goto(0,30)
    pendown()
    for i in range(15):
        pencolor(round(255 + rsoleil), round(23 + gsoleil), round(226 + bsoleil))
        forward(lsoleil)
        backward(2*lsoleil)
        hauteur += 1
        lsoleil += liste1[pliste1]
        pliste1 += 1
        goto(0, hauteur)
        rsoleil += (0)
        gsoleil += (114/101)
        bsoleil += (-203/202)
    forward(lsoleil)
    backward(2*lsoleil)
    penup()
    for i in range(15):
        pencolor(round(255 + rsoleil), round(23 + gsoleil), round(226 + bsoleil))
        forward(lsoleil)
        backward(2*lsoleil)
        hauteur += 1
        lsoleil += liste1[pliste1]
        pliste1 += 1
        goto(0, hauteur)
        rsoleil += (0)
        gsoleil += (114/101)
        bsoleil += (-203/202)
    pendown()
    for i in range(17):
        pencolor(round(255 + rsoleil), round(23 + gsoleil), round(226 + bsoleil))
        forward(lsoleil)
        backward(2*lsoleil)
        hauteur += 1
        lsoleil += liste2[pliste2]
        pliste2 += 1
        goto(0, hauteur)
        rsoleil += (0)
        gsoleil += (114/101)
        bsoleil += (-203/202)
    forward(lsoleil)
    backward(2*lsoleil)
    penup()
    for i in range(17):
        pencolor(round(255 + rsoleil), round(23 + gsoleil), round(226 + bsoleil))
        forward(lsoleil)
        backward(2*lsoleil)
        hauteur += 1
        lsoleil += liste2[pliste2]
        pliste2 += 1
        goto(0, hauteur)
        rsoleil += (0)
        gsoleil += (114/101)
        bsoleil += (-203/202)
    pendown()
    for i in range(17):
        pencolor(round(255 + rsoleil), round(23 + gsoleil), round(226 + bsoleil))
        forward(lsoleil)
        backward(2*lsoleil)
        hauteur += 1
        lsoleil += liste2[pliste2]
        pliste2 += 1
        goto(0, hauteur)
        rsoleil += (0)
        gsoleil += (114/101)
        bsoleil += (-203/202)
    forward(lsoleil)
    backward(2*lsoleil)
    penup()
    for i in range(20):
        pencolor(round(255 + rsoleil), round(23 + gsoleil), round(226 + bsoleil))
        forward(lsoleil)
        backward(2*lsoleil)
        hauteur += 1
        lsoleil += liste2[pliste2]
        pliste2 += 1
        goto(0, hauteur)
        rsoleil += (0)
        gsoleil += (114/101)
        bsoleil += (-203/202)
    pendown()
    pliste2 -= 1
    for i in range(71):
        pencolor(round(255 + rsoleil), round(23 + gsoleil), round(226 + bsoleil))
        forward(lsoleil)
        backward(2*lsoleil)
        hauteur += 1
        lsoleil -= liste2[pliste2]
        pliste2 -= 1
        goto(0, hauteur)
        rsoleil += (0)
        gsoleil += (114/101)
        bsoleil += (-203/202) 
    pliste1 -= 1
    for i in range(30):
        pencolor(round(255 + rsoleil), round(23 + gsoleil), round(226 + bsoleil))
        forward(lsoleil)
        backward(2*lsoleil)
        hauteur += 1
        lsoleil -= liste1[pliste1]
        pliste1 -= 1
        goto(0, hauteur)
        rsoleil += (0)
        gsoleil += (114/101)
        bsoleil += (-203/202)
    forward(lsoleil)

def pavage():
    colormode(255)
    pensize(5)
    speed(0)
    rciel = 0
    gciel = 0 
    bciel = 0
    hauteur = -360
    penup()
    goto(-640,-360)
    pendown()
    while hauteur != 0:
        pencolor(round(15 + rciel), round(4 + gciel), round(76 + bciel))
        forward(1280)
        hauteur += 1
        goto(-640, hauteur)
        rciel += (91/180)
        gciel += (1/36)
        bciel += (7/18)
    pencolor(229, 123, 240)
    pencolor(229, 123, 240)
    #Lignes au dessus du pavage
    pensize(4),penup(),goto(-640,0),pendown(),goto(640,0),pensize(2),penup(),goto(-640, 0),pendown()
    #lignes gauche
    penup(),goto(-20.00,0),pendown(),goto(-60.00,-360.00),penup(),goto(-60.00,0),pendown(),goto(-180.00,-360.00),penup(),goto(-100.00,0),pendown(),goto(-300.00,-360.00),penup(),goto(-140.00,0),pendown(),goto(-420.00,-360.00),penup(),goto(-180.00,0),pendown(),goto(-540.00,-360.00),penup(),goto(-220.00,0),pendown(),goto(-660.00,-360.00),penup(),goto(-260.00,0),pendown(),goto(-780.00,-360.00),penup(),goto(-300.00,0),pendown(),goto(-900.00,-360.00),penup(),goto(-340.00,0),pendown(),goto(-1020.00,-360.00),penup(),goto(-380.00,0),pendown(),goto(-1140.00,-360.00),penup(),goto(-420.00,0),pendown(),goto(-1260.00,-360.00),penup(),goto(-460.00,0),pendown(),goto(-1380.00,-360.00),penup(),goto(-500.00,0),pendown(),goto(-1500.00,-360.00),penup(),goto(-540.00,0),pendown(),goto(-1620.00,-360.00),penup(),goto(-580.00,0),pendown(),goto(-1740.00,-360.00),penup(),goto(-620.00,0),pendown(),goto(-1760.00,-360.00)
    #lignes droites
    penup(),goto(20,0),pendown(),goto(60.00,-360.00),penup(),goto(60.00,0),pendown(),goto(180.00,-360.00),penup(),goto(100.00,0),pendown(),goto(300.00,-360.00),penup(),goto(140.00,0),pendown(),goto(420.00,-360.00),penup(),goto(180.00,0),pendown(),goto(540.00,-360.00),penup(),goto(220.00,0),pendown(),goto(660.00,-360.00),penup(),goto(260.00,0),pendown(),goto(780.00,-360.00),penup(),goto(300.00,0),pendown(),goto(900.00,-360.00),penup(),goto(340.00,0),pendown(),goto(1020.00,-360.00),penup(),goto(380.00,0),pendown(),goto(1140.00,-360.00),penup(),goto(420.00,0),pendown(),goto(1260.00,-360.00),penup(),goto(460.00,0),pendown(),goto(1380.00,-360.00),penup(),goto(500.00,0),pendown(),goto(1500.00,-360.00),penup(),goto(540.00,0),pendown(),goto(1620.00,-360.00),penup(),goto(580.00,0),pendown(),goto(1740.00,-360.00),penup(),goto(620.00,0),pendown(),goto(1760.00,-360.00)
    #Lignes horizontales
    penup(),goto(-640, -300),pendown(),goto(640, -300),penup(),goto(-640, -240),pendown(),goto(640, -240),penup(),goto(-640, -190),pendown(),goto(640, -190),penup(),goto(-640, -140),pendown(),goto(640, -140),penup(),goto(-640, -100),pendown(),goto(640, -100),penup(),goto(-640, -70),pendown(),goto(640, -70),penup(),goto(-640, -40),pendown(),goto(640, -40),penup(),goto(-640, -15),pendown(),goto(640, -15)

def bat1():
    penup()
    rbat = 0
    gbat = 0 
    bbat = 0
    hauteur = 0
    pendown()
    xturtle, yturtle = pos()
    while hauteur != 72:
        pencolor(round(125 + rbat), round(35 + gbat), round(216 + bbat))
        forward(42)
        hauteur += 1
        goto(xturtle, hauteur)
        rbat += (-5/3)
        gbat += (-7/15)
        bbat += (-72/25)
    forward(42)
    penup()
    right(90)
    forward(72)
    left(90)
  
  
def bat2():
    rbat = 0
    gbat = 0 
    bbat = 0
    hauteur = 0
    pendown()
    xturtle, yturtle = pos()
    while hauteur != 50:
        pencolor(round(125 + rbat), round(35 + gbat), round(216 + bbat))
        forward(45)
        hauteur += 1
        goto(xturtle, hauteur)
        rbat += (-5/2)
        gbat += (-7/10)
        bbat += (-108/25)
    forward(45)
    penup()
    right(90)
    forward(50)
    left(90)

def bat3():
    rbat = 0
    gbat = 0 
    bbat = 0
    hauteur = 0
    pendown()
    xturtle, yturtle = pos()
    while hauteur != 90:
        pencolor(round(125 + rbat), round(35 + gbat), round(216 + bbat))
        forward(30)
        hauteur += 1
        goto(xturtle, hauteur)
        rbat += (-25/18)
        gbat += (-7/18)
        bbat += (-12/5)
    forward(30)
    penup()
    right(90)
    forward(90)
    left(90)

def bat4(): 
    rbat = 0
    gbat = 0 
    bbat = 0
    hauteur = 0
    pendown()
    xturtle, yturtle = pos()
    while hauteur != 130:
        pencolor(round(125 + rbat), round(35 + gbat), round(216 + bbat))
        forward(18)
        hauteur += 1
        goto(xturtle, hauteur)
        rbat += (-25/26)
        gbat += (-7/26)
        bbat += (-108/65)
    forward(9)
    left(90)
    forward(20)
    backward(20)
    right(90)
    forward(9)
    penup()
    right(90)
    forward(130)
    left(90)

def ville():
    penup()
    goto(-320,0)
    bat3(), bat2(), bat1(), bat4() ,bat3(), bat4(), bat3(), bat2(), bat1(), bat2(), bat1(), bat3(), bat1(), bat4(), bat2(), bat1(), bat3(), bat1(), bat4(), bat3()

def montagne():
    #montagne derrière la première
    penup()
    goto(-480,0)
    fillcolor(110, 27, 188)
    begin_fill()
    for i in range(3):
        forward(250)
        left(120)
    end_fill()
    
    goto(-480,0)
    pencolor(51, 210, 246)
    ymontagne = 10
    for i in range(11):
        pendown()
        goto(-355,ymontagne)
        goto(-230,0)
        penup()
        goto(-480,0)
        ymontagne += 20
        
    #montagne derrière la deuxième
    penup()
    goto(277,0)
    fillcolor(110, 27, 188)
    begin_fill()
    for i in range(3):
        forward(225)
        left(120)
    end_fill()
    
    goto(277,0)
    pencolor(51, 210, 246)
    ymontagne = 10
    for i in range(10):
        pendown()
        goto(389,ymontagne)
        goto(502,0)
        penup()
        goto(277,0)
        ymontagne += 20
    
    
    #montagne de gauche
    penup()
    goto(-640,0)
    fillcolor(110, 27, 188)
    begin_fill()
    for i in range(3):
        forward(320)
        left(120)
    end_fill()
    
    goto(-640,0)
    pencolor(51, 210, 246)
    ymontagne = 10
    for i in range(14):
        pendown()
        goto(-480,ymontagne)
        goto(-320,0)
        penup()
        goto(-640,0)
        ymontagne += 20
        
   #montagne de droite
    penup()
    goto(364,0)
    fillcolor(110, 27, 188)
    begin_fill()
    for i in range(3):
        forward(350)
        left(120)
    end_fill()
    
    goto(364,0)
    pencolor(51, 210, 246)
    ymontagne = 10
    for i in range(15):
        pendown()
        goto(539,ymontagne)
        goto(714,0)
        penup()
        goto(364,0)
        ymontagne += 20

#appel de toutes les fonctions
fond(), etoile(), soleil(), montagne(), ville(), pavage(), penup(),goto(-640, -40),pendown(),goto(640, -40),penup(),goto(-640, -15),pendown(),goto(640, -15)


#enregistrement de l'image finale avec vérification des modules importés

exitonclick()