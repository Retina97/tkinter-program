import pandas as pd

def verifier(matricule):
    if(matricule ==''):
        return "veillez introduire un matricule"
    etudiants = pd.read_csv('Liste_etudiants.csv', sep=';', encoding='latin-1')
    matricule = int(matricule)
    for m in etudiants['Matricule']:           
        if matricule == m:
            return True
    return False

def ajouter(matricule, nom, prenom):
    if(matricule ==''):
        return "veillez introduire un matricule"
    matricule = int(matricule)
    if (verifier(matricule)):
        return "Etudiant existe deja"   
    if(nom ==''):
        return "veillez introduire un nom"
    if(prenom ==''):
        return "veillez introduire un prenom"    
    with open("Liste_etudiants.csv", "a") as etudiant:
        etudiant.write("%d;%s;%s\n" % (matricule, nom, prenom))
    return "%s %s inscrit avec succes \n" % (nom, prenom)

def moyenne():
    notes = pd.read_csv('Notes_etudiants.csv',index_col='Matricule', sep=';', encoding='latin-1')    
    f = open("Moyenne_etudiants.csv", "w+")
    f.write("Matricule;Moyenne;Admis;Mention\n")
    f.close
    with open("Moyenne_etudiants.csv") as f:
        etudiant=f.readlines()
    for etudiant in notes.iterrows():    
        moyenne = (etudiant[1]['Maths']*3+etudiant[1]['Physique']*2+etudiant[1]['Chimie']*2+etudiant[1]['Informatique']+etudiant[1]['Anglais'])/9
        with open("Moyenne_etudiants.csv", "a") as moyennes:
            if(moyenne>=10):
                if(moyenne >= 10 and moyenne < 12):
                    moyennes.write("%d;%.2f;admis(e);Passable\n" % (etudiant[0], moyenne))
                elif(moyenne >= 12 and moyenne < 14):
                    moyennes.write("%d;%.2f;admis(e);Assez Bien\n" % (etudiant[0], moyenne))
                elif(moyenne >= 14 and moyenne < 16):
                    moyennes.write("%d;%.2f;admis(e);Bien\n" % (etudiant[0], moyenne))
                elif(moyenne >= 16 and moyenne < 18):
                    moyennes.write("%d;%.2f;admis(e);Trés Bien\n" % (etudiant[0], moyenne))
                elif(moyenne >= 18 and moyenne < 20):
                    moyennes.write("%d;%.2f;admis(e);Excellent\n" % (etudiant[0], moyenne))            
            else:
                moyennes.write("%d;%.2f;ajourné(e);\n" % (etudiant[0], moyenne))

def supprimer(matricule):
    if(matricule ==''):
        return "veillez introduire un matricule"
    matricule = int(matricule)
    if (verifier(matricule)):        
        etudiants = pd.read_csv('Liste_etudiants.csv',index_col='Matricule', sep=';', encoding='latin-1')
        etudiants = etudiants.drop(matricule)
        etudiants.to_csv("Liste_etudiants.csv",sep=';', encoding='latin-1')
        return "Etudiant supprimer avec succés"
    else:
        return "Etudiant n'existe pas"
    
def compteur ():
    df = pd.read_csv('Moyenne_etudiants.csv', sep=';', encoding='latin-1')
    return df['Admis'].value_counts()

def listeFinale():    
    etudiants = pd.read_csv('Liste_etudiants.csv', index_col='Matricule', sep=';', encoding='latin-1')
    noteList = pd.read_csv('Notes_etudiants.csv', index_col='Matricule', sep=';', encoding='latin-1')
    try:
        moyennes = pd.read_csv('Moyenne_etudiants.csv', index_col='Matricule', sep=';', encoding='latin-1')                
    except:        
        return "Calculer les moyennees d'abord"
    else:
        f = open("Liste_finale.csv", "a")
        final = pd.concat([etudiants, noteList, moyennes], axis=1, join='inner')
        final.to_csv("Liste_finale.csv",sep=';', encoding='latin-1')
        f.write("Admis;Ajournés\n")
        c = compteur()
        f.write("%d;%d\n" % (c['admis(e)'], c['ajourné(e)']))
        f.close
        return "Liste finale exportée dans Liste_finale.csv"
    
    
    
    