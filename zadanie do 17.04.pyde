def setup():
    global pierwsza_pozycja, druga_pozycja, kolorki, litera_wcisnieta, pierwszy_kolor, drugi_kolor, zmiana_kolorow, pierwsza_litera, druga_litera
    size(500, 400)
    litera_wcisnieta = False
    pierwsza_pozycja = [250, 250]
    druga_pozycja = [300, 250]
    pierwsza_litera = "K"
    druga_litera = "P"
    kolorki = ["#FB7374", "#F5A352"]
    pierwszy_kolor = 0
    drugi_kolor = 0
    textSize(100)
    zmiana_kolorow = False
    noFill()
    stroke("#FF1493")
    circle(325,290,160)
   
def draw():
    if mysz(pierwsza_pozycja[0], pierwsza_pozycja[1]) == True:
        pierwszy_kolor = 1
    else:
        pierwszy_kolor = 0
    if litera_wcisnieta == True:
        drugi_kolor = 1
    else:
        drugi_kolor = 0
    if zmiana_kolorow == True:
        temp = pierwszy_kolor
        pierwszy_kolor = drugi_kolor
        drugi_kolor = temp
    fill(kolorki[pierwszy_kolor])
    text(pierwsza_litera, pierwsza_pozycja[0], pierwsza_pozycja[1] + 75)
    fill(kolorki[drugi_kolor])
    text(druga_litera, druga_pozycja[0] + 40, druga_pozycja[1] + 75)
   
def keyPressed():
    global litera_wcisnieta, zmiana_kolorow
    k = key
    if keyCode == LEFT:
        zmiana_kolorow = True
    if keyCode == RIGHT:
        zmiana_kolorow = True
    if str(k).upper() == druga_litera:
        litera_wcisnieta = True
       
def keyReleased():
    global litera_wcisnieta, zmiana_kolorow
    k = key
    if keyCode == LEFT:
        zmiana_kolorow = False
    if keyCode == RIGHT:
        zmiana_kolorow = False
    if str(k).upper() == druga_litera:
        litera_wcisnieta = False
 
def mysz(a, b):
    if mouseX >= a and mouseX <= a + 75:
        if mouseY >= b and mouseY <= b + 75:
            return True
        else:
            return False
    else:
        return False
