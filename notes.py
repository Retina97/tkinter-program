import pandas as pd
import numpy as np
import etudiant

def verifier(matricule,module):        
    if(matricule ==''):
        return "veillez introduire un matricule"
    matricule = int(matricule)
    if(not etudiant.verifier(matricule)):
        return "Etudiant n'existe pas"
    if(module ==''):
        return "veillez introduire un module"
    noteList = pd.read_csv('Notes_etudiants.csv',index_col='Matricule', sep=';', encoding='latin-1')    
    return not np.isnan(noteList.loc[matricule][module])

def ajouter(matricule,module,note):    
    if(matricule ==''):
        return "veillez introduire un matricule"
    matricule = int(matricule)
    if(module ==''):
        return "veillez introduire un module"
    if(note == ''):
        return "veillez introduire une note"
    temp = verifier(matricule,module)
    if (temp == True):
        return "Note deja inseré"         
    elif(temp== False):        
        noteList = pd.read_csv('Notes_etudiants.csv',index_col='Matricule', sep=';', encoding='latin-1')    
        noteList.loc[matricule][module] = note
        noteList.to_csv("Notes_etudiants.csv",sep=';', encoding='latin-1')
        return "Insersion avec succes\n"
    else: 
        return temp

def supprimer(matricule,module):    
    if(matricule ==''):
        return "veillez introduire un matricule"
    matricule = int(matricule)
    if(module ==''):
        return "veillez introduire un module"
    temp = verifier(matricule,module)
    if (temp == False):
        return "Note n'existe pas"  
    elif(temp == True):               
        noteList = pd.read_csv('Notes_etudiants.csv',index_col='Matricule', sep=';', encoding='latin-1')            
        noteList.loc[matricule][module] = float('NaN')        
        noteList.to_csv("Notes_etudiants.csv",sep=';', encoding='latin-1')
        return "Suppression avec succes\n"
    else:
        return temp

def modifier(matricule,module,note):
    if(matricule ==''):
        return "veillez introduire un matricule"
    matricule = int(matricule)
    if(module ==''):
        return "veillez introduire un module"
    if(note == ''):
        return "veillez introduire une note"
    temp = verifier(matricule,module)
    if (temp == False):
        return "Note n'existe pas"     
    elif(temp == True):       
        noteList = pd.read_csv('Notes_etudiants.csv',index_col='Matricule', sep=';', encoding='latin-1')            
        noteList.loc[matricule][module] = note        
        noteList.to_csv("Notes_etudiants.csv",sep=';', encoding='latin-1')
        return "Modification avec succes\n"
    else:
        return temp

def distribution():
    try:
        df = pd.read_csv('Moyenne_etudiants.csv', sep=';', encoding='latin-1')
    except:        
        return "Calculer les moyennees d'abord"
    else:            
        f = open("Distribution_moyenne.csv", "w+")
        f.write("Intervalle;Distribution\n")
        f.close
        moyennes = df['Moyenne']
        interval = []
        for i in range(21):
            interval.append(i)
        dist, inter = np.histogram(moyennes, bins=interval)
        d = open('Distribution_moyenne.csv', 'a')
        for i in range(20):        
            d.write("%d - %f;%d\n" % (inter[i], inter[i]+0.99, dist[i]))
        d.close
        return "Distribution calculer et Exporter dans Distribution_moyenne.csv"
    
    
    