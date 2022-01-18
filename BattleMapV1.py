from tkinter import *
import csv
from os import chdir
# chdir(r"C:\Users\fabie\Documents\JDR\Entre l'Empire et l'Enfer\Programme BattleMap\Données")

InfoCarte=[] #On définie la liste qui organise le csv
with open("TableauValeurs.csv") as fichier :
    spamreader=csv.reader(fichier, delimiter=';',quotechar='"')
    for row in spamreader:
        InfoCarte.append(row)
    fichier.close
print(InfoCarte)
        
class Battlemaps():
    def __init__(self,fond,TailleX,TailleY):
        self.fenetre=Toplevel()
        self.liste_ob=[]
        self.carte=fond
        self.largeur=TailleX
        self.hauteur=TailleY                                                                        #Def standart d'un canvas
        self.can=Canvas(self.fenetre, width=self.largeur, height=self.hauteur, bg='black') 
        self.can.grid(row=0, column=0)
        self.WP=PhotoImage(file=self.carte, master=self.fenetre)
        self.can.create_image(0,0,anchor=NW,image=self.WP)
        self.frame_bouton=Frame(self.fenetre,bg='#b23519')
        self.frame_bouton.grid(row=1, column=0)
        self.Boutons()
        
        self.can.bind('<Button-1>',self.clic)
        self.fenetre.mainloop() 
        
    def Boutons(self):      #Chaque fonction lance une battlemap (et seulement la carte)
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
        Battlemaps(InfoCarte[2][1],InfoCarte[2][2],InfoCarte[2][3])
    
    def Necropolis(self):
        Battlemaps(InfoCarte[3][1],InfoCarte[3][2],InfoCarte[3][3])
    
    def CampImp(self):
        Battlemaps(InfoCarte[4][1],InfoCarte[4][2],InfoCarte[4][3])
        
    def CampNuit(self):
        Battlemaps(InfoCarte[5][1],InfoCarte[5][2],InfoCarte[5][3])  
        
    def clic(self,event):
        x,y=event.x,event.y
        liste_indice=self.can.find_overlapping(x,y,x+5,y+5) #♦On trouve tous les objets autour du clic
        for i in liste_indice :
            if i>1: #nb de cases
                self.selection=i #l'indice de la pièce sélectionnée
                self.can.bind('<Motion>',self.drag) # association du mouvement de la souris 
                self.piec=trouver_objet(self.liste_ob,i)

    def drag(self,event):
        self.can.coords(self.selection,event.x,event.y) #on bouge la  au fur et à mesure
        self.can.bind('<ButtonRelease-1>',self.unclick)

    def unclick(self,event):
        x,y=event.x,event.y
        indice=self.can.find_overlapping(x,y,x+5,y+5)
        self.piec.MAJ_xy(x,y,self.can)
        self.can.unbind('<Motion>') #on désassocie le mouvement de la souris 
        
def trouver_objet(liste_ob,indice): #Fonction qui sert à permettre le unbind
    for ob in liste_ob:
        if ob.indice==indice :
            return ob    
class objet():
    def __init__(self,x=0,y=0,nf=''):
        self.x=x 
        self.y=y
        self.nom_fichier=nf
        
    def MAJ_xy(self,x,y,can):
        self.x=x
        self.y=y
        can.coords(self.indice,self.x,self.y)

    def MAJ_position(self,ij):
        self.ij=ij

    def creation_image(self,can):
        self.fichier=self.nom_fichier
        self.img=PhotoImage(file=self.fichier)
        self.indice=can.create_image(self.x,self.y,anchor=CENTER,image=self.img) 

Battlemaps(InfoCarte[1][1],InfoCarte[1][2],InfoCarte[1][3])
# Jaskier=objet(300,450,nf="dandelion.png")
# self.liste_ob.append(Jaskier)
# Jaskier.creation_image(self.can)                  #Lignes type pour placer un objet 