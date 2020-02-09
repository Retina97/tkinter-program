from tkinter import *
from tkinter import messagebox

import etudiant
import notes

class MyWindow:
    def __init__(self, win):
        """ ETUDIANT """
        #LABEL
        self.labelEtudiant = Label(win, text='------------ ETUDIANT ------------')
        self.labelEtudiant.place(x=5, y=20)
        
        self.labelMatricule = Label(win, text='Matricule')
        self.labelMatricule.place(x=5, y=50)
        
        self.labelNom = Label(win, text='Nom')
        self.labelNom.place(x=5, y=110)
        
        self.labelPrenom = Label(win, text='Prenom')
        self.labelPrenom.place(x=5, y=140)
                    
        #INPUT
        self.inputMatricule = Entry(bd=3)
        self.inputMatricule.place(x=65, y=50)
        
        self.inputNom = Entry(bd=3)
        self.inputNom.place(x=65, y=110)
        
        self.inputPrenom = Entry(bd=3)
        self.inputPrenom.place(x=65, y=140)
                        
        #BUTTON
        self.buttonVerifier = Button(win, text='Verifier', command=self.e_verifier)      
        self.buttonVerifier.place(x=65, y=78)
        
        self.buttonSupprimer = Button(win, text='Supprimer', command=self.e_supprimer)      
        self.buttonSupprimer.place(x=125, y=78)
        
        self.buttonAjouter = Button(win, text='Ajouter', command=self.e_ajouter)      
        self.buttonAjouter.place(x=100, y=170)
        
        """ NOTES """
        self.labelSeparateur = Label(win, text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|")
        self.labelSeparateur.place(x=220, y=20)
        s1 = '-'*90
        self.labelSeparateur = Label(win, text=s1)
        self.labelSeparateur.place(x=5, y=220)
        
        self.labelNotes = Label(win, text='-------------- NOTES --------------')
        self.labelNotes.place(x=250, y=20)
        #LABEL
        self.labelMatricule2 = Label(win, text='Matricule')
        self.labelMatricule2.place(x=250, y=50)
        
        #self.labelModule = Radiobutton( )
        
        MODULES = {"Maths" : "Maths", 
                  "Phys" : "Physique", 
                  "Chimie" : "Chimie", 
                  "Info" : "Informatique", 
                  "Ang" : "Anglais"} 
           
    
        self.inputModule = StringVar(win, "1") 
        
        b1 = Radiobutton(win, text='Maths', variable=self.inputModule, value='Maths', indicator = 0)        
        b1.place(x=240, y=76)
        b2 = Radiobutton(win, text='Phys', variable=self.inputModule, value='Physique', indicator = 0)        
        b2.place(x=290, y=76)
        b2 = Radiobutton(win, text='Chimie', variable=self.inputModule, value='Chimie', indicator = 0)        
        b2.place(x=330, y=76)
        b2 = Radiobutton(win, text='Info', variable=self.inputModule, value='Informatique', indicator = 0)        
        b2.place(x=385, y=76)
        b2 = Radiobutton(win, text='Ang', variable=self.inputModule, value='Anglais', indicator = 0)        
        b2.place(x=430, y=76)
        
        
        self.inputModule.set("Maths") # initialize    
    
        self.labelNote = Label(win, text='Note')
        self.labelNote.place(x=250, y=140)
                    
        #INPUT
        self.inputMatricule2 = Entry(bd=3)
        self.inputMatricule2.place(x=310, y=50)
        
        #self.inputModule = Entry(bd=3)
        #self.inputModule.place(x=310, y=78)
        
        self.inputNote = Entry(bd=3)
        self.inputNote.place(x=310, y=140)
                        
        #BUTTON
        self.buttonVerifier = Button(win, text='Verifier', command=self.n_verifier)      
        self.buttonVerifier.place(x=310, y=105)
        
        self.buttonSupprimer = Button(win, text='Supprimer', command=self.n_supprimer)      
        self.buttonSupprimer.place(x=370, y=105)
        
        self.buttonAjouter = Button(win, text='Ajouter', command=self.n_ajouter)      
        self.buttonAjouter.place(x=310, y=170)
        
        self.buttonModifier = Button(win, text='Modifier', command=self.n_modifier)      
        self.buttonModifier.place(x=370, y=170)
        
        """ BOUTTONS """
        self.buttonMoyenne = Button(win, text='Calculer les moyennes', command=self.moyenne)      
        self.buttonMoyenne.place(x=70, y=260)
        self.buttonFinale = Button(win, text='Exporter Liste Finale', command=self.finale)      
        self.buttonFinale.place(x=260, y=260)
        self.buttonDist = Button(win, text='Calculer la distribution des moyennes', command=self.dist)      
        self.buttonDist.place(x=130, y=300)

    def dist(self):
        r = notes.distribution()
        messagebox.showinfo("Distribution", r)
    
    def finale(self):
        r = etudiant.listeFinale()
        messagebox.showinfo("Liste Finale", r)
        
    def moyenne(self):
        etudiant.moyenne()
        messagebox.showinfo("Moyennes", "Moyennes calculées et exportées dans Moyenne_etudiants.csv")

                                
    def n_verifier(self):
        r = notes.verifier(self.inputMatricule2.get(), self.inputModule.get())
        if(r == True):            
            messagebox.showinfo("Title", "Module deja introduit")
        else:
            if(r == False):
                messagebox.showwarning("Verification", "Module non introduit")
            else:
                messagebox.showwarning("Verification", r)
    def n_ajouter(self):        
        m = self.inputMatricule2.get()
        mo = self.inputModule.get()
        n = self.inputNote.get()
        r = notes.ajouter(m, mo, n)
        messagebox.showinfo("Ajout", r)    
    def n_supprimer(self):
        m = self.inputMatricule2.get()
        mo = self.inputModule.get()
        r = notes.supprimer(m, mo)
        messagebox.showinfo("Suppression", r)        
    def n_modifier(self):
        m = self.inputMatricule2.get()
        mo = self.inputModule.get()
        n = self.inputNote.get()
        r = notes.modifier(m, mo, n)
        messagebox.showinfo("Modification", r)  
              
    def e_verifier(self):   
        r = etudiant.verifier(self.inputMatricule.get())
        if(r == True):
            messagebox.showinfo("Title", "Etudiant existe")
        elif (r == False):
            messagebox.showwarning("Verification", "Etudiant n'existe pas")
        else:
            messagebox.showwarning("Verification", r)
    def e_ajouter(self):        
        m = self.inputMatricule.get()
        n = self.inputNom.get()
        p = self.inputPrenom.get()
        r = etudiant.ajouter(m, n, p)
        messagebox.showinfo("Ajout", r)        
    def e_supprimer(self):
        m = self.inputMatricule.get()
        r = etudiant.supprimer(m)
        messagebox.showinfo("Suppression", r)
        

window=Tk()
window.minsize(480,360)
window.config(background='#74BDCB')
mywin=MyWindow(window)
window.title('Gestion Scolarité')
window.geometry("480x360")
window.mainloop()