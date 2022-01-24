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
Map1=[31,32,33,34,30,30]
Map2=[31,32,33,34,35,17,17,18]
Map3=[31,32,33,34,35,19,19,20,21,21]
Map4=[31,32,33,34,35,19,19,20,20,20,21,21,21]   #On définit les sets de perso à faire apparaître dans une battlemaps (On fait des 'pack')
Map5=[31,32,33,34,35,26,26,26,26,26]
Map6=[31,32,33,34,35,22,24,24,24]
Map7=[31,32,33,34,35,27,27,27,27,27]
Map8=[31,32,33,34,35,28,28]
Map9=[31,32,33,34,35,23,23,23,23]
Map10=[31,32,33,34,35,25,25,25,25]


class page_acceuil():
    def __init__(self):
        self.fenetre=Tk()
        
        self.frame_battle=LabelFrame(self.fenetre)
        self.frame_battle.grid(row=2,column=1)
        
        self.frame_bouton=Frame(self.fenetre)
        self.frame_bouton.grid(row=1,column=1)
        
        self.frame_camp=LabelFrame(self.frame_bouton)
        self.frame_camp.grid(row=1,column=2)
        
        self.frame_route=LabelFrame(self.frame_bouton)
        self.frame_route.grid(row=1,column=3)
        
        self.Route()
        self.BoutCamp()
        self.Boutons()
        Battlemaps(self.frame_battle,InfoCarte[1][2],InfoCarte[1][3],InfoCarte[1][4],InfoCarte[1][0])
        self.fenetre.mainloop()
        
    def Route(self):
        bouton_Route1=Button(self.frame_route,fg='grey',font='CasablancaAntique',activebackground="white", text="R1", command=self.Route1)
        bouton_Route1.grid(row=1, column=1, padx=2, pady=5)
        bouton_Route2=Button(self.frame_route,fg='grey',font='CasablancaAntique',activebackground="white", text="R2", command=self.Route2)
        bouton_Route2.grid(row=1, column=2, padx=2, pady=5)
        bouton_Route3=Button(self.frame_route,fg='grey',font='CasablancaAntique',activebackground="white", text="R3", command=self.Route3)
        bouton_Route3.grid(row=1, column=3, padx=2, pady=5)     #3 Encounters similaires, je les rassemble
        
    def BoutCamp(self):
        bouton_ALP1=Button(self.frame_camp,fg='grey',font='CasablancaAntique',activebackground="white", text="C1", command=self.Clairiere)
        bouton_ALP1.grid(row=1, column=1, padx=2, pady=5)
        bouton_ALP2=Button(self.frame_camp,fg='grey',font='CasablancaAntique',activebackground="white", text="C2", command=self.Falaise)
        bouton_ALP2.grid(row=1, column=2, padx=2, pady=5)
        bouton_ALP3=Button(self.frame_camp,fg='grey',font='CasablancaAntique',activebackground="white", text="C3", command=self.Cercle_de_Pierre)
        bouton_ALP3.grid(row=1, column=3, padx=2, pady=5)
        bouton_ALP4=Button(self.frame_camp,fg='grey',font='CasablancaAntique',activebackground="white", text="C4", command=self.CampRoute)
        bouton_ALP4.grid(row=1, column=4, padx=2, pady=5)   #Pareil que haut-dessus
        
    def Boutons(self):
        bouton_Sortie=Button(self.frame_bouton,fg='grey',font='CasablancaAntique',activebackground="white", text="Quitter", command=self.fenetre.destroy)
        bouton_Sortie.grid(row=1, column=0, padx=20, pady=5)

        bouton_Nocs=Button(self.frame_bouton,fg='grey',font='CasablancaAntique',activebackground="white", text="Les Nocturnes", command=self.Necropolis)
        bouton_Nocs.grid(row=1, column=7, padx=20, pady=5)

        bouton_CI=Button(self.frame_bouton,fg='grey',font='CasablancaAntique',activebackground="white", text="Marche !", command=self.CampImp)
        bouton_CI.grid(row=1, column=5, padx=20, pady=5)
    
        bouton_TG=Button(self.frame_bouton,fg='grey',font='CasablancaAntique',activebackground="white", text="Manger du Sable", command=self.TG)
        bouton_TG.grid(row=1, column=6, padx=20, pady=5)
        
        bouton_Retour=Button(self.frame_bouton,fg='grey',font='CasablancaAntique',activebackground="white", text="Menu",command=self.Retour)
        bouton_Retour.grid(row=1,column=1,padx=20, pady=5)
        
        bouton_Riviere=Button(self.frame_bouton,fg='grey',font='CasablancaAntique',activebackground="white", text="L'eau",command=self.Riviere)
        bouton_Riviere.grid(row=1,column=8,padx=20, pady=5)
        
        bouton_Hutte=Button(self.frame_bouton,fg='grey',font='CasablancaAntique',activebackground="white", text="Hutte",command=self.Hutte)
        bouton_Hutte.grid(row=1,column=9,padx=20, pady=5)
        
        bouton_Tav=Button(self.frame_bouton,fg='grey',font='CasablancaAntique',activebackground="white", text="La Taverne",command=self.Taverne)
        bouton_Tav.grid(row=1,column=10,padx=20, pady=5)

        bouton_Route=Button(self.frame_bouton,fg='grey',font='CasablancaAntique',activebackground="white", text="En voyage",command=self.Voyage)
        bouton_Route.grid(row=1,column=14,padx=20, pady=5)  #On créer un bouton pour chaque carte.

    def Retour(self):
        Battlemaps(self.frame_battle,InfoCarte[1][2],InfoCarte[1][3],InfoCarte[1][4],InfoCarte[1][0])
    def CampImp(self):
        Battlemaps(self.frame_battle,InfoCarte[2][2],InfoCarte[2][3],InfoCarte[2][4],InfoCarte[2][0]) 
    def TG(self):
        Battlemaps(self.frame_battle,InfoCarte[3][2],InfoCarte[3][3],InfoCarte[3][4],InfoCarte[3][0])
    def Necropolis(self):
        Battlemaps(self.frame_battle,InfoCarte[4][2],InfoCarte[4][3],InfoCarte[4][4],InfoCarte[4][0])
    def Clairiere(self):
        Battlemaps(self.frame_battle,InfoCarte[5][2],InfoCarte[5][3],InfoCarte[5][4],InfoCarte[5][0])  
    def Falaise(self):
        Battlemaps(self.frame_battle,InfoCarte[6][2],InfoCarte[6][3],InfoCarte[6][4],InfoCarte[6][0])
    def Cercle_de_Pierre(self):
        Battlemaps(self.frame_battle,InfoCarte[7][2],InfoCarte[7][3],InfoCarte[7][4],InfoCarte[7][0])
    def CampRoute(self):
        Battlemaps(self.frame_battle,InfoCarte[8][2],InfoCarte[8][3],InfoCarte[8][4],InfoCarte[8][0])
    def Route1(self):
        Battlemaps(self.frame_battle,InfoCarte[9][2],InfoCarte[9][3],InfoCarte[9][4],InfoCarte[9][0])
    def Route2(self):
        Battlemaps(self.frame_battle,InfoCarte[10][2],InfoCarte[10][3],InfoCarte[10][4],InfoCarte[10][0])
    def Route3(self):
        Battlemaps(self.frame_battle,InfoCarte[11][2],InfoCarte[11][3],InfoCarte[11][4],InfoCarte[11][0])
    def Riviere(self):
        Battlemaps(self.frame_battle,InfoCarte[12][2],InfoCarte[12][3],InfoCarte[15][4],InfoCarte[12][0])
    def Hutte(self):
        Battlemaps(self.frame_battle,InfoCarte[13][2],InfoCarte[13][3],InfoCarte[13][4],InfoCarte[13][0])
    def Taverne(self):
        Battlemaps(self.frame_battle,InfoCarte[14][2],InfoCarte[14][3],InfoCarte[14][4],InfoCarte[14][0])
    def Voyage(self):
        Battlemaps(self.frame_battle,InfoCarte[15][2],InfoCarte[15][3],InfoCarte[15][4],InfoCarte[15][0])

class Battlemaps():
    def __init__(self,frame,fond,TailleX,TailleY,Num): #je te rajoute la frame dans laquelle on va dessiner le canvas
        self.liste_ob=[]
        self.Num=Num
        self.carte=fond
        self.largeur=TailleX
        self.hauteur=TailleY                                                                        #Def standart d'un canvas
        self.can=Canvas(frame, width=self.largeur, height=self.hauteur, bg='black') 
        self.can.grid(row=0, column=0)
        self.WP=PhotoImage(file=self.carte, master=frame)
        self.can.create_image(0,0,anchor=NW,image=self.WP)
        self.Spawn()
        self.can.bind('<Button-1>',self.clic)    
        frame.mainloop()
        
    def Spawn(self):        #On fait apparaître différents objets en se servant du nom de la carte et de la carte associée
        if self.Num==InfoCarte[3][0]:
            for i in range(0,len(Map1)):
                self.Crea(Map1[i])
        elif self.Num==InfoCarte[4][0]:
            for i in range(0,len(Map2)):
                self.Crea(Map2[i])
        elif self.Num==InfoCarte[5][0]:
            for i in range(0,len(Map3)):
                self.Crea(Map3[i])
        elif self.Num==InfoCarte[6][0]:
            for i in range(0,len(Map3)):
                self.Crea(Map3[i])
        elif self.Num==InfoCarte[7][0]:
            for i in range(0,len(Map4)):
                self.Crea(Map4[i])
        elif self.Num==InfoCarte[8][0]:
            for i in range(0,len(Map3)):
                self.Crea(Map3[i])
        elif self.Num==InfoCarte[9][0]:
            for i in range(0,len(Map5)):
                self.Crea(Map5[i])
        elif self.Num==InfoCarte[10][0]:
            for i in range(0,len(Map6)):
                self.Crea(Map6[i])
        elif self.Num==InfoCarte[11][0]:
            for i in range(0,len(Map7)):
                self.Crea(Map7[i])
        elif self.Num==InfoCarte[12][0]:
            for i in range(0,len(Map8)):
                self.Crea(Map8[i])
        elif self.Num==InfoCarte[13][0]:
            for i in range(0,len(Map9)):
                self.Crea(Map9[i])
        elif self.Num==InfoCarte[14][0]:
            for i in range(0,len(Map10)):
                self.Crea(Map10[i])
            
    def Crea(self,NumListe):
        Nom=objet(InfoCarte[NumListe][2],InfoCarte[NumListe][3],InfoCarte[NumListe][4])
        self.liste_ob.append(Nom)
        Nom.creation_image(self.can) #Création d'un objet et on le stock dans une liste pour le faire bouger
        
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
    def __init__(self,nf='',x=0,y=0):
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
        
page_acceuil()

