class Pared:
    def __init__(self,orientacion):
        self.orientacion = orientacion
        self.superfici = 0

    def trampitas(self,superficie):
        self.superficie = superficie


class Ventana:
    def __init__(self,pared,superficie,proteccion):
        self.superficie = superficie
        self.orientacion = pared.orientacion
        if proteccion!="Persiana" and proteccion!="Estor":
            raise Exception("Exception: Protección obligatoria ")



        

class Casa:

    paredes=[["NORTE",0],["OESTE",0],["SUR",0],["ESTE",0]]

    def __init__(self,paredes):
        self.norte = paredes[0].orientacion
        self.oeste = paredes[1].orientacion
        self.sur = paredes[2].orientacion
        self.este = paredes[3].orientacion

        self.sup_norte = paredes[0].superficie
        self.sup_oeste = paredes[1].superficie
        self.sup_sur = paredes[2].superficie
        self.sup_este = paredes[3].superficie


    

    def superficie_acristalada(self):
        return self.paredes[0][1]+self.paredes[1][1]+self.paredes[2][1]+self.paredes[3][1]
        

class ParedCortina():
    def __init__(self,orientacion,superficie):
        self.orientacion = orientacion
        self.superficie = superficie





pared_norte = Pared("NORTE") 
pared_oeste = Pared("OESTE") 
pared_sur = Pared("SUR") 
pared_este = Pared("ESTE") 

ventana_norte = Ventana(pared_norte, 0.5,"Estor") 
ventana_oeste = Ventana(pared_oeste, 1,"Estor") 
ventana_sur = Ventana(pared_sur, 2,"Estor") 
ventana_este = Ventana(pared_este, 1,"Estor") 

pared_norte.trampitas(ventana_norte.superficie)
pared_oeste.trampitas(ventana_oeste.superficie)
pared_sur.trampitas(ventana_sur.superficie)
pared_este.trampitas(ventana_este.superficie)

pared_norte1 = ParedCortina("NORTE",0.5) 
pared_oeste1 = ParedCortina("OESTE",1) 
pared_sur1 = ParedCortina("SUR",2) 
pared_este1 = ParedCortina("ESTE",1)






print(pared_este1.orientacion)

#print(ventana_norte.orientacion)
#print(pared_norte.orientacion)

casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])

casa.paredes[0] = ["NORTE", ventana_norte.superficie]
casa.paredes[1] = ["OESTE", ventana_oeste.superficie]
casa.paredes[2] = ["SUR", ventana_sur.superficie]
casa.paredes[3] = ["ESTE", ventana_este.superficie]

#print(casa.norte)

print(casa.superficie_acristalada()) 

#print(casa.paredes)

casa.paredes[2] = ["SUR", 10]

#print(casa.paredes)

print(casa.superficie_acristalada()) 


