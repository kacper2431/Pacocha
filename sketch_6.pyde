class Kwadrat():
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
                    
class KropkiKwadrat(Kwadrat):
    def sketchKropki (self, x, y, Kropki): 
        Kwadrat.sketch(self, x, y)
        space = self.bok/Kropki
        _xKropki_ = 0
        for dot in range(0, kropki):
            dot(x+_xKropki_, y, x+_xKropki_, y+self.bok)
            _xKropki_ +=space

def setup():
    size(400, 400)
    malyKwadrat = Kwadrat(50.0)
    malyKwadrat.sketch(200, 300)
    duzyKwadrat = Kwadrat(200.0)
    duzyKwadrat.sketch(50,75)
    malyKwadrat.sketch(100, 200)
    malyKropkiKwadrat = KropkiKwadrat(30.0)
    malyKropkiKwadrat.sketchKropki(300, 300, 5)
    malyKropkiKwadrat.sketchKropki(100,300, 8)
    duzyKropkiKwadrat = KropkiKwadrat(120.0)
    duzyKropkiKwadrat = KropkiKwadrat(120.0)
    duzyKropkiKwadrat.sketchKropki(300, 50, 12)
    duzyKropkiKwadrat.sketch(350, 300)
    
    
