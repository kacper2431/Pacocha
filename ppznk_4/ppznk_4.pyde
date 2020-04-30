import random
add_library('pdf')

def setup():
    global img, img2, img3
    size(400, 400) # to nie są proporcje dowodowego zdjęcia
    #size(400, 400, PDF, "czwarte.pdf")
    img = loadImage("dowodowefoto.jpg")
    img2 = loadImage("unnamed.png")
    img3 = loadImage("unnamed2.png")
    beginRecord(PDF, "outczwarte.pdf")
    
    print(random.random())
    print(type(img))
    fill(20,255,200)
    
def draw():
    global img, img2, img3
    image(img, 0,0, height, width)
    #img2(unnamed, 0,0, height/2, width/2)
    ##img3(unnamed2, 0,0, height/2, width/2)
    
    if key == "1": # warto byłoby zakomunikować użytkownikowi jak wybrać dodatek
        image(img2, 90,80, 220, 200)
    if key == "2":
        image(img3, 90,80, 220, 200)

def mousePressed():
    endRecord()
    exit()
    
# 1,75p
      
