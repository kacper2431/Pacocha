def setup ():
  size (400,600) 
  point (50,50)
  rectMode (CORNERS)


def draw ():
    if mousePressed:
        circle (mouseX, mouseY, height/4) # warto używać zależnych zamiast sztywnych wartości
    # miało też coś innego się zadziać gdy się nie klika
#1,5pkt
