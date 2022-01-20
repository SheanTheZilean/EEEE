from tkinter import *
import csv
from os import chdir
chdir(r"C:\Users\fabie\Documents\JDR\Entre l'Empire et l'Enfer\Programme BattleMap\Données")

InfoCarte=[] #On définie la liste qui organise le csv
with open("TableauValeurs.csv") as fichier :
    spamreader=csv.reader(fichier, delimiter=';',quotechar='"')
    for row in spamreader:
        InfoCarte.append(row)
    fichier.close
print(InfoCarte)

class page_acceuil():
    def __init__(self):
        self.fenetre=Tk()
        
        self.frame_battle=LabelFrame(self.fenetre, text="Ici la battlemap")
        self.frame_battle.grid(row=2,column=1)
        
        self.frame_bouton=Frame(self.fenetre)
        self.frame_bouton.grid(row=1,column=1)

        self.Boutons()
        Battlemaps(self.frame_battle,InfoCarte[1][1],InfoCarte[1][2],InfoCarte[1][3])
        self.fenetre.mainloop()
        
        
    def Boutons(self):
        bouton_Sortie=Button(self.frame_bouton,fg='grey',font='CasablancaAntique',activebackground="white", text="Quitter", command=self.fenetre.destroy)
        bouton_Sortie.grid(row=1, column=1, padx=20, pady=5)

        bouton_Nec=Button(self.frame_bouton,fg='grey',font='CasablancaAntique',activebackground="white", text="Entrée", command=self.Entree)
        bouton_Nec.grid(row=1, column=2, padx=20, pady=5)

        bouton_Nocs=Button(self.frame_bouton,fg='grey',font='CasablancaAntique',activebackground="white", text="Les Nocturnes", command=self.Necropolis)
        bouton_Nocs.grid(row=1, column=3, padx=20, pady=5)

        bouton_CI=Button(self.frame_bouton,fg='grey',font='CasablancaAntique',activebackground="white", text="Marche !", command=self.CampImp)
        bouton_CI.grid(row=1, column=4, padx=20, pady=5)

        bouton_ALP=Button(self.frame_bouton,fg='grey',font='CasablancaAntique',activebackground="white", text="La Brume", command=self.CampNuit)
        bouton_ALP.grid(row=1, column=5, padx=20, pady=5)
        
        
        

    def Entree(self):
        Battlemaps(self.frame_battle,InfoCarte[2][1],InfoCarte[2][2],InfoCarte[2][3])

    def Necropolis(self):
        Battlemaps(self.frame_battle,InfoCarte[3][1],InfoCarte[3][2],InfoCarte[3][3])

    def CampImp(self):
        Battlemaps(self.frame_battle,InfoCarte[4][1],InfoCarte[4][2],InfoCarte[4][3])

    def CampNuit(self):
        Battlemaps(self.frame_battle,InfoCarte[5][1],InfoCarte[5][2],InfoCarte[5][3])  
        
        
        

class Battlemaps():
    def __init__(self,frame,fond,TailleX,TailleY): #je te rajoute la frame dans laquelle on va dessiner le canvas
        self.liste_ob=[]
        self.carte=fond
        self.largeur=TailleX
        self.hauteur=TailleY                                                                        #Def standart d'un canvas
        self.can=Canvas(frame, width=self.largeur, height=self.hauteur, bg='black') 
        self.can.grid(row=0, column=0)
        self.WP=PhotoImage(file=self.carte, master=frame)
        self.can.create_image(0,0,anchor=NW,image=self.WP)       
        frame.mainloop()
page_acceuil()