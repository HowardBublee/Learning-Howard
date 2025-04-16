
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
    def __init__(self, Marke:str, Modell:str, BJ:str,MotorLeistungW:int,Reichweitekm:int):
        super().__init__(Marke, Modell, BJ)
        
        self.MotorleistungW=MotorLeistungW
        self.Reichweitekm=Reichweitekm
        
e_Auto=Elektroauto("Audi","A6","1969",200,1600)
print(e_Auto.URL)
print(e_Auto.marke)      