
class Auto:
    def __init__(self,Marke,Modell,BJ):
        self.marke=Marke
        self.Modell=Modell
        self.BJ=BJ
        self.URL= "URL"
    
p=Auto("Audi","A6","1969")
print(p.marke)
print(p.BJ)

class Elektroauto(Auto):
    def __init__(self, Marke, Modell, BJ,MotorLeistung,Reichweite):
        super().__init__(Marke, Modell, BJ)
        
        self.Motorleistung=MotorLeistung
        self.Reichweite=Reichweite
        
e_Auto=Elektroauto("Audi","A6","1969","200W","1600")
print(e_Auto.URL)
print(e_Auto.marke)      