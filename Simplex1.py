

import numpy as np
class Max:
    
    def __init__(self):
        self.nb_variables=0
        self.nb_contraintes=0
        self.coeffition=[]
        self.comparaison=[]
        self.liste_contrainte=[]

    def enter(self):
        self.nb_variables=int(input("Nombre de variable "))
        self.nb_contraintes=int(input("Nombre de contraintes ?: "))
        self.table=np.zeros((self.nb_contraintes+1, self.nb_variables + self.nb_variables+2))
        print(self.table) #création du tableau à valeurs nulles
        if self.nb_variables==2:
            self.deuxvariables()
    
    def deuxvariables(self):
        [self.x0,self.y0, self.e10,self.e20,self.Z0,self.b0]=[int(input("Coeff de x dans Z: ")),int(input("Coeff de y dans Z: ")),0,0,1,0]
        self.table[0,0]=self.x0
        self.table[0,1]=self.y0
        self.table[0,2]=self.e10
        self.table[0,3]=self.e20
        self.table[0,4]=self.Z0
        self.table[0,5]=self.b0
        
        [self.x1,self.y1, self.e11,self.e21,self.Z1,self.b1]=[int(input("Coeff de x dans 1ere contrainte: ")),int(input("Coeff de y dans 1ere contrainte: ")),1,0,1,0]
        self.table[1,0]=self.x1
        self.table[1,1]=self.y1
        self.table[1,2]=self.e11
        self.table[1,3]=self.e21
        self.table[1,4]=self.Z1
        self.table[1,5]=self.b1
        
        [self.x2,self.y2, self.e12,self.e22,self.Z2,self.b2]=[int(input("Coeff de x dans 2e contrainte: ")),int(input("Coeff de y dans 2e contrainte: ")),0,0,1,0]
        self.table[1,0]=self.x2
        self.table[1,1]=self.y2
        self.table[1,2]=self.e12
        self.table[1,3]=self.e22
        self.table[1,4]=self.Z2
        self.table[1,5]=self.b2
        
    #ATTENTION NB DE E1 E2 EN FONCTION DU NB DE CONTRAINTE ET PAS DE VARIABLE 
        print(self.table)
        
        self.test1()
        
    def troisvariables(self):
        
        [self.x0,self.y0, self.z0, self.e10,self.e20,self.e30,self.Z0,self.b0]=[int(input("Coeff de x dans Z: ")),int(input("Coeff de y dans Z: ")),int(input("Coeff de z dans Z: ")),0,0,0,1,0]
        self.table[0,0]=self.x0
        self.table[0,1]=self.y0
        self.table[0,2]=self.z0
        self.table[0,3]=self.e10
        self.table[0,4]=self.e20
        self.table[0,5]=self.e30
        self.table[0,6]=self.Z0
        self.table[0,7]=self.b0
        
        [self.x1,self.y1, self.z1, self.e11,self.e21,self.e31,self.Z1,self.b1]=[int(input("Coeff de x dans 1ere contrainte: ")),int(input("Coeff de y dans 1ere contrainte: ")),int(input("Coeff de z dans 1ere contrainte: ")),0,0,0,1,0]
        self.table[1,0]=self.x1
        self.table[1,1]=self.y1
        self.table[1,2]=self.z1
        self.table[1,3]=self.e11
        self.table[1,4]=self.e21
        self.table[1,5]=self.e31
        self.table[1,6]=self.Z1
        self.table[1,7]=self.b1
        
        [self.x2,self.y2, self.z2, self.e12,self.e22,self.e32,self.Z2,self.b2]=[int(input("Coeff de x dans 2e contrainte: ")),int(input("Coeff de y dans 2e contrainte: ")),int(input("Coeff de z dans 2e contrainte: ")),0,0,0,1,0]
        self.table[1,0]=self.x2
        self.table[1,1]=self.y2
        self.table[1,2]=self.z2
        self.table[1,3]=self.e12
        self.table[1,4]=self.e22
        self.table[1,5]=self.e32
        self.table[1,6]=self.Z2
        self.table[1,7]=self.b2
        
        [self.x3,self.y3, self.z3, self.e13,self.e23,self.e33,self.Z3,self.b3]=[int(input("Coeff de x dans 3e contrainte: ")),int(input("Coeff de y dans 3e contrainte: ")),int(input("Coeff de z dans 3e contrainte: ")),0,0,0,1,0]
        self.table[1,0]=self.x3
        self.table[1,1]=self.y3
        self.table[1,2]=self.z3
        self.table[1,3]=self.e13
        self.table[1,4]=self.e23
        self.table[1,5]=self.e33
        self.table[1,6]=self.Z3
        self.table[1,7]=self.b3
        
        print(self.table)
    
    def test1(self):
        self.booleen=self.table[0]<0 #s'il y a un coef negatif a la premiere ligne la variable devient True, False sinon
        print(self.booleen)
        self.nb_negtf=self.booleen.count() #nb de variable negatives dans la premiere ligne 
        if self.nb_negtf>0:
            print("Il est tjrs possible d'optimiser le pb")
        else:
            print("Optimisation terminée")


    
    def choix_pivot(table):

        colonne_choices = [(i,x) for (i,x) in enumerate(table[-1][:-1]) if x > 0]
        colonne = min(colonne_choices, key=lambda a: a[1])[0]

        if all(ligne[colonne] <= 0 for ligne in table):
            print ( "probleme")

              
    def contraintes(self):
        self.nb_c=int(input("Combien de contraintes ? "))
        for i in range (self.nb_c):
            self.liste_contrainte.append(input("contrainte n"+str(i+1)+": "))
            coefc = [
                float(
                    input(
                        "saisir coefficient  n "
                        + str(j + 1)
                        + " : "
                    )
                )
                for j in range(self.nb_v)
            ]

            self.coeffition.append(coefc)
            self.comparaison.append(float(input(str(self.liste_contrainte[i]))))

        
    
obj1=Max()
obj1.enter()

